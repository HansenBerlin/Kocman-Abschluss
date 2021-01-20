from ImageData import ImageData
from AvailableOptionsModel import AvailableOptionsModel

class ViewController(object):    

    def __init__(self):   
        self.imageData = ImageData()  
        self.currentPage = 1
        self.availableOptionsData = AvailableOptionsModel()   


    def updatePageAndElementsOnNextButtonClick(self, buttonClicked):
        self.currentPage+=1
        self.updateAvailableOptions(buttonClicked)


    def updatePageAndElementsOnPreviousButtonClick(self, buttonClicked):
        self.currentPage-=1
        if self.currentPage == 1: buttonClicked = 1 
        self.updateAvailableOptions(buttonClicked)


    def updateButtonIcon(self, button):
        if self.currentPage == 1:
            if button == 1: return self.imageData.buttonUsedForOne
            elif button == 2: return self.imageData.buttonUsedForTwo
            elif button == 3: return self.imageData.buttonUsedForThree
        elif self.currentPage == 2:
            if button == 1: return self.imageData.buttonMoneyOne
            elif button == 2: return self.imageData.buttonMoneyTwo
            elif button == 3: return self.imageData.buttonMoneyThree


    def updateButtonValues(self, button, returnTextValue, returnHeaderValue):
        print(self.availableOptionsData.allOptions[self.currentPage-1][3][button-1])
        if returnTextValue: return self.availableOptionsData.allOptions[self.currentPage-1][1][button-1]
        elif returnHeaderValue: return self.availableOptionsData.allOptions[self.currentPage-1][0]
        else: return self.availableOptionsData.allOptions[self.currentPage-1][3][button-1]



    def updateAvailableOptions(self, buttonClicked):
        if self.currentPage == 1:                           
            self.availableOptionsData.price[3] = [False, False, False] #reset all values
            self.availableOptionsData.sizeAndWeight[3] = [False, False, False] 
            self.availableOptionsData.batteryLife[3] = [False, False, False] 

        elif self.currentPage == 2:            
            if buttonClicked == 2 :
                self.availableOptionsData.price[3][0] = True
                self.availableOptionsData.sizeAndWeight[3][0] = True
                self.availableOptionsData.batteryLife[3][2] = True
                self.availableOptionsData.savedConfigurations[0][1][3][0] = True
                self.availableOptionsData.savedConfigurations[0][2][3][0] = True
                self.availableOptionsData.savedConfigurations[0][3][3][2] = True

            elif buttonClicked == 3: self.availableOptionsData.price[3][0] = True

        elif self.currentPage == 3:            
            if buttonClicked == 1:
                self.availableOptionsData.sizeAndWeight[3][2] = True
                self.availableOptionsData.batteryLife[3][2] = True

        elif self.currentPage == 4:            
            if buttonClicked == 2:
                self.availableOptionsData.batteryLife[3][2] = True
            elif buttonClicked == 3:
                self.availableOptionsData.batteryLife[3][1] = True
                self.availableOptionsData.batteryLife[3][2] = True

   

    def updateWindowElements(self, window):
        keyArray = ['buttonOne', 'buttonTwo', 'buttonThree', 'textInfoButtonOne', 'textInfoButtonTwo', 'textInfoButtonThree', 'headingLeftColumn']
        for x in range(3):
            window[keyArray[x]].update(image_data=self.updateButtonIcon(x+1))            
            window[keyArray[x]].update(disabled=self.updateButtonValues(x+1, False, False))
            window[keyArray[x+3]].update(self.updateButtonValues(x+1, True, False))
        window[keyArray[6]].update(self.updateButtonValues(0, False, True))

                     
            

             
         



        





    


    
