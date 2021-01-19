from ImageData import ImageData
from AvailableOptionsModel import AvailableOptionsModel
from inspect import currentframe
import PySimpleGUI as gui

class ViewController(object):    

    def __init__(self):   
        self.imageData = ImageData()     
        self.buttonOne = gui.Button('', image_data=self.imageData.price, border_width=2, key='buttonOne')
        self.buttonTwo = gui.Button('', image_data=self.imageData.price, border_width=2, key='buttonTwo')
        self.buttonThree = gui.Button('', image_data=self.imageData.price, border_width=2, key='buttonThree')
        self.currentPage = 1
        self.availableOptionsData = AvailableOptionsModel()   


    def clickNextButton(self, buttonClicked):
        self.currentPage+=1
        self.updateAvailableOptions(buttonClicked)


    def updateButtonIcon(self, button):
        if self.currentPage == 2:
            if button == 1: return self.imageData.categories


    def updateOptions(self, button):
        print(self.availableOptionsData.allOptions[self.currentPage-1][3][button-1])
        return self.availableOptionsData.allOptions[self.currentPage-1][3][button-1]


    def updateAvailableOptions(self, buttonClicked):
        if self.currentPage == 2:
            if(buttonClicked == 1):
                self.availableOptionsData.category[3] = [True, True, True, True, True]
            elif(buttonClicked == 2):
                self.availableOptionsData.category[3] = [False, True, True, True, True]
         



        





    


    
