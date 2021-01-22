class ConfigurationController(object):  

    def updatePartIndexValues(self, parts, props):
        
        #Anpassen der Indexwerte je nach Nutzerauswahl anhand untenstehender Tabelle
        lookupColumn = 0       
        while lookupColumn<18:    
            for j in range(8):
                parts[j]+=indexChangesTable[j][props[lookupColumn][2]-1]
                lookupColumn+=3
        for i in range(8):
            print(parts[i])



'''            |   Leist.  |   Preis   |  Groesse  |   Akku    |  Lauts.   |  Robusth |'''
indexChangesTable=[
'''CPU'''      [-1,  1,  2, -1,  2,  1,  0 , 0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0],
'''GPU'''      [-1,  1,  2, -1,  0,  1, -2 , 0,  0, -1,  0,  0, -2, -1,  0,  0,  0,  0],
'''Akku'''     [ 0,  0,  0, -1,  0,  1,  1 , 0, -1, -1,  1,  2,  0,  0,  0,  0,  1,  1],
'''Speicher''' [-1,  1,  2, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],
'''Robusth.''' [ 0,  0,  0, -1,  0,  1,  0 , 0,  0,  0,  0,  0,  0,  0,  0, -1,  1,  2],
'''Lautst.'''  [ 0,  0,  0,  0,  0,  0,  0 , 0,  1,  0,  0,  0, -3, -2,  0,  1, -1,  1],
'''Gew.'''     [ 0,  1,  0,  0,  0,  0, -1 , 0,  1,  0,  1,  2,  0,  0,  0,  0,  0,  0],
'''Preis'''    [ 0,  0,  0, -1,  1,  3,  0 , 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]






    




