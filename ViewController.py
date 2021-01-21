from CombineOptionsController import CombineOptionsController
from ImageData import ImageData
from AvailableOptionsModel import AvailableOptionsModel

class ViewController(object):    

    def __init__(self):  
        self.currentPage = 0
        self.imageData = ImageData()  
        self.propsData = AvailableOptionsModel()  
        self.mainController = CombineOptionsController(self.propsData) 


    def updatePageAndElementsOnNextButtonClick(self, buttonClicked, window):
        if self.currentPage < 7:
            if self.currentPage != 0: self.mainController.updateAvailableOptions(self.propsData, buttonClicked, self.currentPage)
            self.updateLeftColumnElements(window)
            self.updateRightColumnElements(window)
            self.currentPage+=1
        #currentpage war vorher in erster Zeile



    def updatePageAndElementsOnPreviousButtonClick(self, buttonClicked, window):
        #if self.currentPage == 1: buttonClicked = 1 
        #self.updateAvailableOptions(buttonClicked)
        self.mainController.updateAvailableOptions(self.propsData, buttonClicked, self.currentPage-1)

        self.updateLeftColumnElements(window)
        self.updateRightColumnElements(window)
        self.currentPage-=1
        #CP war vorher in erster Zeile



    def updateButtonValues(self, button, returnTextValue, returnHeaderValue):
        if returnTextValue: return self.propsData.allOptions[self.currentPage][1][button]
        elif returnHeaderValue: return self.propsData.allOptions[self.currentPage][0]
        else:
            #print(self.propsData.allOptions[self.currentPage][3][button]) 
            print(self.propsData.allOptions[self.currentPage][3][button]) 
            return self.propsData.allOptions[self.currentPage][3][button]        


    def updateAvailableOptions(self, buttonClicked):

        # Speichern der Auswahl im Array
        print('Option to set; Button Clicked-1; Updated Option')
        print(self.propsData.allOptions[self.currentPage-1][2])
        print(buttonClicked-1)
        self.propsData.allOptions[self.currentPage-1][2] = buttonClicked-1
        print(self.propsData.allOptions[self.currentPage-1][2])

        self.mainController.updateAvailableOptions(self.propsData)
    

    def updateLeftColumnElements(self, window):
        #später löschen, nur damit nach page 6 kein Fehler kommt
        if self.currentPage >= 7: return -1

        keyArray = ['buttonOne', 'buttonTwo', 'buttonThree', 'textInfoButtonOne', 'textInfoButtonTwo', 'textInfoButtonThree', 'headingLeftColumn', 'textInfoUserSelection']
        for i in range(3):
            window[keyArray[i]].update(image_data=self.imageData.buttonImageDictionary[self.currentPage+1][i])            
            window[keyArray[i]].update(disabled=self.updateButtonValues(i, False, False))
            window[keyArray[i+3]].update(self.updateButtonValues(i, True, False))
        window[keyArray[6]].update(self.updateButtonValues(0, False, True)) 


    def updateRightColumnElements(self, window):
        self.propsData.savedConfigurations = []
        for i in range(6):
            self.propsData.savedConfigurations.append(self.propsData.userSelection[i+1][(self.propsData.allOptions[i][2])-1])  
        window['textInfoUserSelection'].update("\n".join(self.propsData.savedConfigurations))

            




                     
            

             
         



        





    


    
