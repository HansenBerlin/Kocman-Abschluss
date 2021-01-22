class ConfigurationController(object):  

    


    def updatePartIndexValues(self, propsData): 
        #Anpassen der Indexwerte je nach Nutzerauswahl anhand untenstehender Tabelle
        lookupColumn = 0       
        for i in range(6):
            for j in range(8):
                if propsData.savedButtonChoices[i] != 4:
                    #print(indexChangesTable[j][userSelection[i]-1+lookupColumn])
                    #print(indexChangesTable[j][userSelectionList[i]])

                    propsData.partIndexValues[j] += indexChangesTable[j][propsData.savedButtonChoices[i]-1+lookupColumn]                
                    lookupColumn+=3  


#             |   Leist.  |   Preis   |  Groesse  |   Akku    |  Lauts.   |  Robusth |
indexChangesTable=[
                [-1,  1,  2, -1,  2,  1,  0 , 0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0],
                [-1,  1,  2, -1,  0,  1, -2 , 0,  0, -1,  0,  0, -2, -1,  0,  0,  0,  0],
                [ 0,  0,  0, -1,  0,  1,  1 , 0, -1, -1,  1,  2,  0,  0,  0,  0,  1,  1],
                [-1,  1,  2, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],
                [ 0,  0,  0, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0, -1,  1,  2],
                [ 0,  0,  0,  0,  0,  0,  0 , 0,  1,  0,  0,  0, -3, -2,  0,  1, -1,  1],
                [ 0,  1,  0,  0,  0,  0, -1 , 0,  1,  0,  1,  2,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0, -1,  1,  3,  0 , 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]






    




