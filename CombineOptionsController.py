class CombineOptionsController(object):    

    '''Hauptlogik zur Steuerung der Buttons die ausgegraut werden. Die Laufvariable ist dabei die Seite,
    selection repräsentiert den Button der gedrückt wurde. Der zweite Indexwert der jeweiligen Kategorie zwischen
    0 und 2 ist der eingespeicherte Button für diese Runde. Diese Werte werden in allOptions[x][3] zusammengefasst.
    Nach jedem Event wird der Array mit den Optionen genullt und aktualisiert um die Interaktion vorwärts und 
    rückwärts zu ermöglichen. Index 3 von allOptions ist keine Präferenz, also kein gedrückter Button'''

    def __init__(self, props):   
        self.propsData = props

    def updateAvailableOptions(self, propsData, buttonClicked, page):
        propsData.allOptions[page-1][2] = buttonClicked
        for i in range(6):
            propsData.allOptions[i][3] = [False, False, False, False]  

        for i in range(1,7):   

            selection = (propsData.allOptions[i-1][2])

            if i == 1:   
                if selection == 1:
                    propsData.durability[3][2] = True
                elif selection == 2 :
                    propsData.price[3][0] = True
                    propsData.sizeAndWeight[3][0] = True
                    propsData.batteryLife[3][2] = True
                    propsData.noiseEmission[3][1] = True
                    propsData.noiseEmission[3][2] = True
                    propsData.durability[3][2] = True                    
                elif selection == 3: 
                    propsData.price[3][0] = True

            elif i == 2:     
                if selection == 1:
                    propsData.sizeAndWeight[3][2] = True
                    propsData.batteryLife[3][2] = True
                    propsData.durability[3][1] = True
                    propsData.durability[3][2] = True
                elif selection == 2 :                
                    propsData.durability[3][2] = True                
                elif selection == 3: 
                    propsData.price[3][0] = True

            elif i == 3:
                if selection == 1:
                    propsData.durability[3][2] = True          
                elif selection == 2:
                    propsData.batteryLife[3][2] = True
                    propsData.durability[3][2] = True 
                elif selection == 3:
                    propsData.batteryLife[3][1] = True
                    propsData.batteryLife[3][2] = True
                    propsData.noiseEmission[3][2] = True

            elif i == 4: 
                if selection == 3:
                    propsData.durability[3][2] = True  

            elif i == 5:    
                if selection == 3:
                    propsData.durability[3][2] = True  
        

