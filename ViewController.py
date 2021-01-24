from FinalPartsConfigurationController import FinalPartsConfigurationController
from RadarChartBuilder import RadarChartBuilder
from ConfigurationController import ConfigurationController
from AvailableOptionsModel import AvailableOptionsModel
from CombineOptionsController import CombineOptionsController
from ImageDataModel import ImageData
from FinalPartsConfigurationController import FinalPartsConfigurationController


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
        11:'btnConfirmAndFinish',
        12:'plotCanvas',
        13:'confirmationSelectionOne',
        14:'confirmationSelectionTwo',
        15:'confirmationSelectionThree'             
        }


class ViewController(object):    

    def __init__(self):  
        self.currentPage = 0
        self.imageData = ImageData()
        self.propsData = AvailableOptionsModel()
        self.mainController = CombineOptionsController(self.propsData) 
        self.configController = ConfigurationController()
        self.plotBuilder = RadarChartBuilder()
        self.finalNotebookData = FinalPartsConfigurationController()

   
    def updatePageAndElementsOnNextButtonClick(self, buttonClicked, window):
        if self.currentPage < 7:
            if self.currentPage != 0: 
                self.mainController.updateAvailableOptions(self.propsData, buttonClicked, self.currentPage)
            self.updatePlotOnCanvas(buttonClicked, window, False)
            self.currentPage+=1
            self.updateLeftColumnElements(window)
            self.updateRightColumnElements(buttonClicked, window)                   


    def updatePageAndElementsOnPreviousButtonClick(self, buttonClicked, window):  
        self.mainController.updateAvailableOptions(self.propsData, buttonClicked, self.currentPage)
        self.updatePlotOnCanvas(buttonClicked, window, False) 
        self.currentPage-=1
        self.updateLeftColumnElements(window)
        self.updateRightColumnElements(4, window)  


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
        window[keyDic[10]].update(image_data = self.imageData.buttonNoPreference)       


    def updateRightColumnElements(self, buttonClicked, window):
        self.propsData.allOptions[self.currentPage-1][2] = buttonClicked
        self.propsData.savedConfigurations = []

        for i in range(6):
            self.propsData.savedConfigurations.append(self.propsData.userSelection[i+1][(self.propsData.allOptions[i][2])-1])  

        window[keyDic[8]].update("\n".join(self.propsData.savedConfigurations))
        AvailableOptionsModel.setFinalConfigState(self.propsData.savedConfigurations, self.propsData.partIndexValues)


    def checkPrevAndNextButtonStates(self, buttonClicked, window):
        if buttonClicked != 4: window[keyDic[10]].update(image_data = self.imageData.buttonNext)
        else: window[keyDic[10]].update(image_data = self.imageData.buttonNoPreference)

        if self.currentPage == 1: window[keyDic[9]].update(disabled=True)
        else: window[keyDic[9]].update(disabled=False)

        if self.currentPage == 6: 
            window[keyDic[10]].update(visible=False)
            window[keyDic[11]].update(visible=True)
        else: 
            window[keyDic[10]].update(visible=True)
            window[keyDic[11]].update(visible=False)
   

    def updatePlotOnCanvas(self, buttonClicked, window, finalView):
        if not finalView: self.propsData.savedButtonChoices[self.currentPage-1]=buttonClicked
        self.configController.updatePartIndexValues(self.propsData)
        
        if finalView: self.plotBuilder.buildRadarChart(self.plotBuilder.createDataSet(AvailableOptionsModel.getSavedIndexValues()))
        else: self.plotBuilder.buildRadarChart(self.plotBuilder.createDataSet(self.propsData.partIndexValues))  

        window[keyDic[12]].update('ressources/radarplotUserSelection.png')


    def updateTicks(self, buttonClicked, window):
        for i in range(3): window[keyDic[i+13]].update('ressources/placeholderTick.png')
        if buttonClicked != 4: window[keyDic[buttonClicked+12]].update('ressources/tick.png')


    def updateComponentsInFinalView(self, window, keyDict):
        self.finalNotebookData.adjustIndexValues()
        finalComponentList = self.finalNotebookData.createConfigArray()
        self.updatePlotOnCanvas(-1, window, True)
        window[keyDict[0]].update(finalComponentList[4])
        window[keyDict[1]].update(finalComponentList[0])
        window[keyDict[2]].update(finalComponentList[8])
        window[keyDict[3]].update(finalComponentList[5])
        window[keyDict[4]].update(finalComponentList[7])
        window[keyDict[5]].update(finalComponentList[2])
        window[keyDict[6]].update(finalComponentList[6])
        window[keyDict[7]].update(finalComponentList[3])
        window[keyDict[8]].update(finalComponentList[1])
        window['textRightColumnInfoFinalSelection'].update("\n".join(AvailableOptionsModel.getFinalConfigState()))


        


