class ConfigurationController(object):  

    '''Die Funktion erstellt anhand untenstehender Matrix ausgehend von den Eingaben des Nutzers
    die Indexwerte für den Graph und als spätere Grundlage der Teileauswahl. Pro Eingabe wird durch die 
    Zeile iteriert, jeweils in 3er Schritten +- Eingabe, und der Wert angepasst. Beispiel: Es wurde eine 
    hohe Leistung gewünscht (Zeile 0,  Spalte 2: Wert 3), der Basiswert von 3 wird also auf 6 gesetzt.'''
    
    def updatePartIndexValues(self, propsData): 
        propsData.partIndexValues = [3,3,3,3,3,3,3,3]         

        for i in range(8):
            lookupColumn = 0 
            for j in range(6):
                if propsData.savedButtonChoices[j] != 4:  
                    propsData.partIndexValues[i] += indexChangesTable[i][propsData.savedButtonChoices[j]-1+lookupColumn]                
                lookupColumn+=3          


#               |   Leist.  |   Preis   |  Groesse  |   Akku    |  Lauts.   |  Robusth |
indexChangesTable=[
                [-1,  1,  3, -1,  1,  2, -1 , 0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0],   # CPU
                [-1,  1,  2, -1,  1,  2,  1 , 0,  1, -1,  0,  1, -1,  0,  1, -1,  1,  2],   # Preis
                [ 0,  1,  0,  0,  0,  0, -2 , 0,  2,  0,  1,  2,  0,  0,  0,  0,  0,  1],   # Gewicht
                [ 0,  2,  1,  1,  0, -1,  1 , 0,  0,  0,  0,  0,  1, -1, -3,  0, -1,  1],   # Geräusch
                [ 0,  1,  1, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0, -1,  1,  3],   # Robustheit
                [-1,  1,  2, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],   # Speicher
                [ 0, -2, -1, -1,  0,  1,  0 ,-1, -2, -1,  1,  2,  0,  0,  0,  0,  1,  0],   # Akku
                [-1,  3,  2, -1,  0,  2, -2 ,-1,  0,  0,  0,  0,  0, -1, -3,  0,  0,  0]]   # GPU
                









    




