from FinalNotebookModel import FinalNotebookModel
from AvailableOptionsModel import AvailableOptionsModel


class FinalPartsConfigurationController:
    
    def __init__(self):
        self.indexValues = AvailableOptionsModel.getSavedIndexValues()
        self.notebookModel = FinalNotebookModel()


    '''Diese Funktion erstellt aus den Dictionarys der Notebook Datenklasse eine Liste mit den finalen, konkreten Teilen
    die verbaut werden sollen. Dabei werden noch einige Anpassungen des Preises und der Grafikkarte vorgenommen  '''
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
                    # Anpassen des Preises um 20 bzw 50% nach oben wenn Business oder Outdoor/Spezial ausgewählt wird
                    if AvailableOptionsModel.getFinalConfigState()[5] == 'Business-Level':
                        finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]*1.2)
                    elif AvailableOptionsModel.getFinalConfigState()[5] == 'Outdoor/Special':
                        finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]]*1.5)
                    else: finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[i][self.indexValues[i]])

                elif i == 7:
                    # Anpassen der Grafikkarte im hohen Qualitätssegment je nach angegebenen Nutzen (normale bzw. Workstationkarte)
                    # und bei einer Konfiguration mit hoher Grafikleistung und geringer Lautstärke Anpassen des Lüfters
                    if AvailableOptionsModel.getFinalConfigState()[0] == 'Professional':
                        finalConfigurationOnView.append(self.notebookModel.dictionaryCollection[7][self.indexValues[i]])
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

