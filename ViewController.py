from ImageData import ImageData
from AvailableOptionsModel import AvailableOptionsModel

class ViewController(object):    

    def __init__(self):   
        self.imageData = ImageData()  
        self.currentPage = 1
        self.propsData = AvailableOptionsModel()   


    def updatePageAndElementsOnNextButtonClick(self, buttonClicked):
        self.currentPage+=1
        self.updateAvailableOptions(buttonClicked)


    def updatePageAndElementsOnPreviousButtonClick(self, buttonClicked):
        self.currentPage-=1
        if self.currentPage == 1: buttonClicked = 1 
        self.updateAvailableOptions(buttonClicked)


    def updateButtonValues(self, button, returnTextValue, returnHeaderValue):
        #print(self.propsData.allOptions[self.currentPage-1][3][button-1])
        if returnTextValue: return self.propsData.allOptions[self.currentPage-1][1][button-1]
        elif returnHeaderValue: return self.propsData.allOptions[self.currentPage-1][0]
        else: return self.propsData.allOptions[self.currentPage-1][3][button-1]

        


    def updateAvailableOptions(self, buttonClicked):

        # Speichern der Auswahl im Array
        self.propsData.allOptions[self.currentPage-1][2] = buttonClicked 
        print(self.propsData.allOptions[self.currentPage-1][2])   

        #Zurücksetzen aller Werte wenn der User auf Seite 1 ist / resettet
        if self.currentPage == 1:    
            for i in range(6):
                self.propsData.allOptions[i][3] = [False, False, False]    

        # Anpassung nach Auswahl Anwendungsgebiet
        elif self.currentPage == 2:   
            if buttonClicked == 1:
                self.propsData.durability[3][2] = True
            elif buttonClicked == 2 :
                self.propsData.price[3][0] = True
                self.propsData.sizeAndWeight[3][0] = True
                self.propsData.batteryLife[3][2] = True
                self.propsData.noiseEmission[3][1] = True
                self.propsData.noiseEmission[3][2] = True
                self.propsData.durability[3][2] = True
                #self.propsData.savedConfigurations[0][1][3][0] = True
                #self.propsData.savedConfigurations[0][2][3][0] = True
                #self.propsData.savedConfigurations[0][3][3][2] = True
            elif buttonClicked == 3: 
                self.propsData.price[3][0] = True

        # Anpassung nach Auswahl Preis
        elif self.currentPage == 3:            
            if buttonClicked == 1:
                self.propsData.sizeAndWeight[3][2] = True
                self.propsData.batteryLife[3][2] = True
                self.propsData.durability[3][1] = True
                self.propsData.durability[3][2] = True
            elif buttonClicked == 2 :                
                self.propsData.durability[3][2] = True                
            elif buttonClicked == 3: 
                self.propsData.price[3][0] = True

        # Anpassung nach Auswahl Gewicht und Größe
        elif self.currentPage == 4:  
            if buttonClicked == 1:
                self.propsData.noiseEmission[3][2] = True
                self.propsData.durability[3][2] = True          
            elif buttonClicked == 2:
                self.propsData.batteryLife[3][2] = True
                self.propsData.durability[3][2] = True 
            elif buttonClicked == 3:
                self.propsData.batteryLife[3][1] = True
                self.propsData.batteryLife[3][2] = True
                self.propsData.noiseEmission[3][2] = True

        # Anpassung nach Auswahl Akku
        elif self.currentPage == 5: 
            if buttonClicked == 3:
                self.propsData.durability[3][2] = True  

        # Anpassung nach Auswahl Lautstärke
        elif self.currentPage == 6:             
            if buttonClicked == 3:
                self.propsData.durability[3][2] = True  



    def updateWindowElements(self, window):
        keyArray = ['buttonOne', 'buttonTwo', 'buttonThree', 'textInfoButtonOne', 'textInfoButtonTwo', 'textInfoButtonThree', 'headingLeftColumn', 'textInfoUserSelection']
        for i in range(3):
            window[keyArray[i]].update(image_data=self.imageData.buttonImageDictionary[self.currentPage][i])            
            window[keyArray[i]].update(disabled=self.updateButtonValues(i+1, False, False))
            window[keyArray[i+3]].update(self.updateButtonValues(i+1, True, False))
        window[keyArray[6]].update(self.updateButtonValues(0, False, True))
        if self.currentPage != 1:
            window[keyArray[7]].update(self.propsData.userSelection[self.currentPage-1] [self.propsData.allOptions[self.currentPage-2][2]-1])
            print(self.propsData.userSelection[self.currentPage-1] [self.propsData.allOptions[self.currentPage-2][2]-1])



                     
            

             
         



        





    


    
