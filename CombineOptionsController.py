class CombineOptionsController(object):    

    def __init__(self, props):   
        self.propsData = props
        #self.propsData2 = AvailableOptionsModel()


    def updateAvailableOptions(propsData, buttonClicked, page):

        propsData.allOptions[page-1][2] = buttonClicked
        # aktuelle Auswahl auf dieser Seite wird im Array gespeichert    
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
                    propsData.noiseEmission[3][2] = True
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
        

