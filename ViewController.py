from CombineOptionsController import CombineOptionsController
from ImageData import ImageData
from AvailableOptionsModel import AvailableOptionsModel
from RadarChartBuilder import RadarChartBuilder


keyDic = {
        1: 'buttonOne',
        2: 'buttonTwo',
        3: 'buttonThree',
        4: 'textInfoButtonOne',
        5: 'textInfoButtonTwo',
        6: 'textInfoButtonThree',
        7: 'headingLeftColumn',
        8: 'textRightColumnInfoSelection',
        9: 'buttonPrevious',
        10:'buttonNext',
        11:'fgfgfgfgfdsdfgfghghjdrhrthgd',
        12:'plotCanvas'                
        }

class ViewController(object):    

    def __init__(self):  
        self.currentPage = 0
        self.imageData = ImageData()
        self.propsData = AvailableOptionsModel()
        self.mainController = CombineOptionsController(self.propsData) 
        self.plotSimpleSelection = RadarChartBuilder()

             

    def updatePageAndElementsOnNextButtonClick(self, buttonClicked, window):
        if self.currentPage < 7:
            if self.currentPage != 0: self.mainController.updateAvailableOptions(self.propsData, buttonClicked, self.currentPage)
            self.currentPage+=1
            self.updateLeftColumnElements(window)
            self.updateRightColumnElements(window)            


    def updatePageAndElementsOnPreviousButtonClick(self, buttonClicked, window):        
        self.mainController.updateAvailableOptions(self.propsData, buttonClicked, self.currentPage)
        self.currentPage-=1
        self.updateLeftColumnElements(window)
        self.updateRightColumnElements(window)        


    def updateButtonValues(self, button, returnTextValue, returnHeaderValue):
        if returnTextValue: return self.propsData.allOptions[self.currentPage-1][1][button]
        elif returnHeaderValue: return self.propsData.allOptions[self.currentPage-1][0]
        else: return self.propsData.allOptions[self.currentPage-1][3][button]  


    def updateLeftColumnElements(self, window):
        for i in range(3):
            window[keyDic[i+1]].update(image_data=self.imageData.buttonImageDictionary[self.currentPage][i])            
            window[keyDic[i+1]].update(disabled=self.updateButtonValues(i, False, False))
            window[keyDic[i+4]].update(self.updateButtonValues(i, True, False))
        window[keyDic[7]].update(self.updateButtonValues(0, False, True)) 


    def updateRightColumnElements(self, window):
        self.propsData.savedConfigurations = []
        for i in range(6):
            self.propsData.savedConfigurations.append(self.propsData.userSelection[i+1][(self.propsData.allOptions[i][2])-1])  
        window[keyDic[8]].update("\n".join(self.propsData.savedConfigurations))


    def checkPrevAndNextButtonStates(self, window):
        if self.currentPage == 1: window[keyDic[9]].update(disabled=True)
        else: window[keyDic[9]].update(disabled=False)
        if self.currentPage == 6: 
            window[keyDic[10]].update(visible=False)
            window[keyDic[11]].update(visible=True)
        else: 
            window[keyDic[10]].update(visible=True)
            window[keyDic[11]].update(visible=False)

    #def updatePlotOnCanvas(self, window):        
        #window[keyDic[12]].update(data=self.plotSimpleSelection.image)

