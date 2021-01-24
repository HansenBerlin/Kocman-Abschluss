class ConfigurationController(object):  

    def updatePartIndexValues(self, propsData): 
        #Anpassen der Indexwerte je nach Nutzerauswahl anhand untenstehender Tabelle   
        propsData.partIndexValues = [3,3,3,3,3,3,3,3]         
       # propsData.partIndexValues = [8,8,8,8,8,8,8,8]         

        for i in range(8):
            lookupColumn = 0 
            for j in range(6):
                if propsData.savedButtonChoices[j] != 4:  
                    propsData.partIndexValues[i] += indexChangesTable[i][propsData.savedButtonChoices[j]-1+lookupColumn]                
                lookupColumn+=3  
        print('------------------------------------------')        
        print('indexed values after updating in config controller')
        print(propsData.partIndexValues)
        print('------------------------------------------')


#               |   Leist.  |   Preis   |  Groesse  |   Akku    |  Lauts.   |  Robusth |
indexChangesTable=[
                [-1,  1,  3, -1,  1,  2, -1 , 0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0],   # CPU
                [-1,  0,  0, -1,  1,  3,  1 , 0,  1, -1,  0,  1, -1,  0,  1, -1,  1,  2],   # Preis
                [ 0,  1,  0,  0,  0,  0, -2 , 0,  2,  0,  1,  2,  0,  0,  0,  0,  0,  1],   # Gewicht
                [ 0,  1,  2,  1,  0, -1,  1 , 0,  0,  0,  0,  0,  1, -1, -3,  0, -1,  1],   # Geräusch
                [ 0,  1,  1, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0, -1,  1,  3],   # Robustheit
                [-1,  1,  2, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],   # Speicher
                [ 0, -2, -1, -1,  0,  1,  0 ,-1, -2, -1,  1,  2,  0,  0,  0,  0,  1,  0],   # Akku
                [-1,  2,  2, -1,  0,  1, -2 ,-1,  0,  0,  0,  0,  0, -1, -3,  0,  0,  0]]   # GPU
                









    




