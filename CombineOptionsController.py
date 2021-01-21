from AvailableOptionsModel import AvailableOptionsModel


class CombineOptionsController(object):    

    def __init__(self, props):   
        self.propsData = props
        self.propsData2 = AvailableOptionsModel()


    def updateAvailableOptions(self, propsData, buttonClicked, page):

        propsData.allOptions[page-1][2] = buttonClicked
        # aktuelle Auswahl auf dieser Seite wird im Array gespeichert        

        for i in range(1,7):   

            selection = (propsData.allOptions[i-1][2])
            #propsData.allOptions[i-1][3] = [False, False, False, False]    

            if i == 1:   
                print('debug selection on page ' +str(i)+ ' is: ' +str(selection))
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
                print('debug selection on page ' +str(i)+ ' is: ' +str(selection))       
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
                print('debug selection on page ' +str(i)+ ' is: ' +str(selection))
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
                print('debug selection on page ' +str(i)+ ' is: ' +str(selection))
                if selection == 3:
                    propsData.durability[3][2] = True  

            elif i == 5:    
                print('debug selection on page ' +str(i)+ ' is: ' +str(selection))         
                if selection == 3:
                    propsData.durability[3][2] = True  

        print('\nDebug props Data Object Test')
        print(propsData.allOptions[5][3][3])
        print(self.propsData.allOptions[5][3][3])
        print(self.propsData2.allOptions[5][3][3])
        print('\n')

