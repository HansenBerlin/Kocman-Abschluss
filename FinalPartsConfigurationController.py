from FinalNotebookModel import FinalNotebookModel
from AvailableOptionsModel import AvailableOptionsModel


class FinalPartsConfigurationController:
    
    def __init__(self):
        self.indexValues = AvailableOptionsModel.getSavedIndexValues()
        self.notebookModel = FinalNotebookModel()


    '''Diese Funktion erstellt aus den Dictionarys der Notebook Datenklasse eine Liste mit den finalen, konkreten Teilen
    die verbaut werden sollen. Dabei werden noch einige Anpassungen des Preises und der Grafikkarte vorgenommen'''    
    def createConfigArray(self):
            finalConfigurationOnView = []   

            # Wenn Grafikleistung respektive Prozessorleistung in definierten Wertebereichen liegen
            # wird dem Dictionary fürs Lüftersystem am jeweiligen Wert der GPU/CPU Lüfter hinzugefügt
            if 4 <= self.indexValues[7] <= 6: self.notebookModel.dictionaryCollection[3][self.indexValues[3]] += ', 1*GPU'
            elif self.indexValues[7] > 6: self.notebookModel.dictionaryCollection[3][self.indexValues[3]] += ', 2*GPU'
            if self.indexValues[0] > 3: self.notebookModel.dictionaryCollection[3][self.indexValues[3]] += ', 1*CPU'
            
            for i in range(8):
                # Anpassen von Extremwerten
                if self.indexValues[i]<0: self.indexValues[i] = 0
                elif self.indexValues[i]>8: self.indexValues[i] = 8

                if i == 1:
                    # Anpassen des Preises um 10 bzw 30% nach oben wenn Business oder Outdoor/Spezial ausgewählt wird
                    if AvailableOptionsModel.getFinalConfigState()[5] == 'Business-Level':
                        finalConfigurationOnView.append(round(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]*1.1, 2))
                    elif AvailableOptionsModel.getFinalConfigState()[5] == 'Outdoor/Special':
                        finalConfigurationOnView.append(round(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]*1.3, 2))
                    else: finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]])

                elif i == 7:
                    # Anpassen der Grafikkarte im hohen Qualitätssegment je nach angegebenen Nutzen (normale bzw. Workstationkarte)
                    # und bei einer Konfiguration mit hoher Grafikleistung und geringer Lautstärke Anpassen des Lüfters
                    if AvailableOptionsModel.getFinalConfigState()[0] == 'Professional':
                        finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]])
                    else: finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]) 

                # Anpassen aller restlichen Werte bis auf den Ram (außerhalb der Listenlänge)
                else: finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]])

            # Anpassen des Rams angelehnt an gewählte Gesamtleistung
            finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[8][self.indexValues[0]])

            return finalConfigurationOnView

    
    '''Anpassung der Indexwerte um ein letztes mal den Plot zu aktualisieren und unplausible Kombinationen zu vermeiden'''
    def adjustIndexValues(self):
        self.indexValues[1] = self.adjustPrice()
        # Sind bei der Auswahl hohe Werte bei GPU und CPU Leistung herausgekommen, wird analog zu 
        # den zusätzlichen Lüftern in der Konfiguration der Indexwert der Lautstärkeentwicklung erhöht
        if 4 <= self.indexValues[7] <= 6: self.indexValues[3]+=1
        elif self.indexValues[7] > 6: self.indexValues[3]+=2
        if self.indexValues[0] > 3: self.indexValues[3]+=1

        # wenn Outdoor/Special gewählt wurde und der Akkuindexwert sehr niedrig ist, den Indexwert der Akkuleistung nach oben anpassen
        if AvailableOptionsModel.getFinalConfigState()[5]=='Outdoor/Special' and self.indexValues[6] < 3: self.indexValues[6]+=2


    '''Insbesondere wenn Konfigurationen mit Extremwerten nach oben und unten entstehen, aber auch wenn oft keine Präferenz gewählt wird,
    können unplausible Ergebnisse entstehen. Mit dieser Methode wird ein Gleichgewicht der Indexwerte mit dem Preis verglichen, um diesen
    dann ggfs nach oben oder unten anzupassen. Wurde bei Preis etwas ausgewählt, wird dies hier mit bereinigt'''

    # Liste Reihenfolge ['Rechenleistung', 'Preis', 'Gewicht', 'Lautstärke', 'Robustheit', 'Speicher', 'Akku', 'Grafikleistung'] 
    def adjustPrice(self):
            priceOption = AvailableOptionsModel.getFinalConfigState()[1]
            price = 0
            
            for i in range(8):
                if i == 0:
                    price += (self.indexValues[i]-4)*2                   
                elif i in (2,3): 
                    price += (4-self.indexValues[i])/1.5                    
                elif i in (4,5,6): 
                    price += (self.indexValues[i]-4)                    
                elif i == 7:
                    price += (self.indexValues[i]-4)*1.5
                   
            price = round(price, 0)

            if priceOption == 'niedrig': price+=1
            elif priceOption == 'mittel': price-=1
            elif priceOption == 'hoch': price-=2

            if price <= -10: return 1
            elif price <= -5: return 2
            elif price <= 0: return 3
            else: return round((price+self.indexValues[1])/2, 0)
            

    '''Die Benchmarkwerte für das letzte Fenster werden aus den Indexwerten mit unterschiedlichen Gewichtungen errechnet
    und auf 100 hochgerechnet (weil der Maximalwert bei 54 liegt und somit als Referenz dient). Extremwerte im Highendbereich 
    werden mit Bonuspunkten belohnt'''
    def calculateFinalBenchmark(self):
        indexValue = 0
        for i in range(8):
            if i == 0:
                indexValue += (self.indexValues[i])-1*2.3   
                if self.indexValues[i]==8: indexValue+=15    
            elif i in (2,3): 
                indexValue += 8-self.indexValues[i]      
                if self.indexValues[i]==1: indexValue+=2          
            elif i == 4:
                indexValue += self.indexValues[i]-1  
                if self.indexValues[i]==8: indexValue+=5
            elif i in (5,6): 
                indexValue += (self.indexValues[i]-1)*1.2   
                if self.indexValues[i]==8: indexValue+=5               
            elif i == 7:
                indexValue += (self.indexValues[i]-1)*1.5
                if self.indexValues[i]==8: indexValue+=10          

        return int(round(indexValue*1.818, 0))

