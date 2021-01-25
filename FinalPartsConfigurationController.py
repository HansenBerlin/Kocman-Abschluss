from FinalNotebookModel import FinalNotebookModel
from AvailableOptionsModel import AvailableOptionsModel


class FinalPartsConfigurationController:
    
    def __init__(self):
        self.indexValues = AvailableOptionsModel.getSavedIndexValues()
        self.notebookModel = FinalNotebookModel()


    '''Diese Funktion erstellt aus den Dictionarys der Notebook Datenklasse eine Liste mit den finalen, konkreten Teilen
    die verbaut werden sollen. Dabei werden noch einige Anpassungen des Preises und der Grafikkarte vorgenommen,
    am Preis insbesondere dann wenn keine Präferenzen angegeben wurden'''    
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
                        finalConfigurationOnView.append(round(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]*1.1, 0))
                    elif AvailableOptionsModel.getFinalConfigState()[5] == 'Outdoor/Special':
                        finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]*1.3)
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
        # Sind bei der Auswahl hohe Werte bei GPU und CPU Leistung herausgekommen, wird analog zu 
        # den zusätzlichen Lüftern in der Konfiguration der Indexwert der Lautstärkeentwicklung erhöht
        if 4 <= self.indexValues[7] <= 6: self.indexValues[3]+=1
        elif self.indexValues[7] > 6: self.indexValues[3]+=2
        if self.indexValues[0] > 3: self.indexValues[3]+=1

        # wenn Outdoor/Special gewählt wurde und der Akkuindexwert sehr niedrig ist, den Indexwert der Akkuleistung nach oben anpassen
        if AvailableOptionsModel.getFinalConfigState()[5]=='Outdoor/Special' and self.indexValues[6] < 3: self.indexValues[6]+=2

        self.indexValues[1] = self.adjustPriceTwo()

    
    def adjustPrice(self):
        price = 0
        for i in range(8):
            if i not in (1,2,3):
                price += self.indexValues[i]
                print('{}{}'.format('price raised to', price))
            elif i != 1: 
                price -= self.indexValues[i]
                print('{}{}'.format('price reduced to', price))
        if price != 0: price = round(price/5, 0)
        else: price = 0

        # abfangen, dass das Ergebnis plus Preis nicht kleiner als 1 ist
        print('{}{}'.format('at index:', self.indexValues[1]))

        if price + self.indexValues[1] < 1: return 1
        else: return price + self.indexValues[1]  


    def adjustPriceTwo(self):
        priceOption = AvailableOptionsModel.getFinalConfigState()[1]
        priceUp = 0
        priceDown = 0
        finalAdjustmentCalc = 0
        for i in range(8):
            if i not in (1,2,3):
                priceUp += self.indexValues[i]
                print('{}{}'.format('price raised to', priceUp))
            elif i != 1: 
                priceDown += self.indexValues[i]
                print('{}{}'.format('price reduced to', priceDown))
        priceUp = round(priceUp/5, 0)
        priceDown = round(priceDown/3, 0)

        print('{}{}'.format('PriceChange:', priceUp-priceDown))

        finalAdjustmentCalc = priceUp-priceDown
        if priceOption == 'niedrig': finalAdjustmentCalc+=1
        elif priceOption == 'mittel': finalAdjustmentCalc-=1
        elif priceOption == 'hoch': finalAdjustmentCalc-=2

        print('{}{}'.format('final PriceChange:', finalAdjustmentCalc))
        print('{}{}'.format('actual Price:', self.indexValues[1]))

        #Preis irgendwie vergleichen/Faktor? Also Ergebnis müsste eigentlich dem aktuellen Preis entsprechen?


        if finalAdjustmentCalc+self.indexValues[1]<1: return 1
        else: return finalAdjustmentCalc+self.indexValues[1]
    
    # Liste Reihenfolge ['Rechenleistung', 'Preis', 'Gewicht', 'Lautstärke', 'Robustheit', 'Speicher', 'Akku', 'Grafikleistung']    


