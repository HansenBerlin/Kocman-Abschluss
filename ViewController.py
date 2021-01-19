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
        self.updateAvailableOptions(buttonClicked)


    def updateButtonIcon(self, button):
        if self.currentPage == 2:
            if button == 1: return self.imageData.categories


    def updateButtonState(self, button):
        print(self.availableOptionsData.allOptions[self.currentPage-1][3][button-1])
        return self.availableOptionsData.allOptions[self.currentPage-1][3][button-1]


    def updateAvailableOptions(self, buttonClicked):
        if self.currentPage == 2:
            if(buttonClicked == 1):
                self.availableOptionsData.category[3] = [False, True, True]
            elif(buttonClicked == 2):
                self.availableOptionsData.category[3] = [False, False, True]
            elif(buttonClicked == 3):
                self.availableOptionsData.category[3] = [False, False, False]
         



        





    


    
