from ViewController import ViewController
from AvailableOptionsModel import AvailableOptionsModel
from ImageData import ImageData
import PySimpleGUI as gui

testModel = AvailableOptionsModel()
viewController = ViewController()
imageData = ImageData()  

buttonPrevious = gui.Button('PREVOUS', image_data=imageData.buttonPrevious, size=(14,1.0), key='buttonPrevious', button_color=('white', '#66bb6a'), pad=([80,40],[0,0]))
buttonNext = gui.Button('NEXT', image_data=imageData.buttonNext, size=(14,1.0), key='buttonNext', button_color=('white', '#66bb6a'))
buttonOne = gui.Button('', image_data=imageData.buttonUsedForOne, key='buttonOne', button_color=('white', '#66bb6a'), pad=([81,26],[0,0]))
buttonTwo = gui.Button('', image_data=imageData.buttonUsedForTwo, key='buttonTwo', button_color=('white', '#66bb6a'), pad=([0,26],[0,0]))
buttonThree = gui.Button('', image_data=imageData.buttonUsedForThree, key='buttonThree', button_color=('white', '#66bb6a'))

infoTextButtonOne =   gui.Text('                                                                                                     \n \n \n \n \n \n', 
                    font='Consolas 8', background_color='#cee1cf', text_color='black', key='textInfoButtonOne', pad=([81,0],[20,50]))
infoTextButtonTwo =   gui.Text('                                                                                                     \n \n \n \n \n \n', 
                    font='Consolas 8', background_color='#cee1cf', text_color='black', key='textInfoButtonTwo', pad=([0,26],[20,50]))
infoTextButtonThree =   gui.Text('                                                                                                   \n \n \n \n \n \n', 
                    font='Consolas 8', background_color='#cee1cf', text_color='black', key='textInfoButtonThree', pad=([0,0],[20,50]))
infoTextRowNamesUserSelection = gui.Text('Anwendung/Leistung \nPreis \nGewicht und Größe \nAkkulaufzeit \nLautstärke \nRobustheit \n',
                    font='Consolas 10', background_color='#cee1cf', text_color='black', pad=([50,0],[0,0]))
infoTextCurrentUserSelection =   gui.Text('                                                                                          \n \n \n \n \n \n', 
                    font='Consolas 10', background_color='#cee1cf', text_color='black', key='textInfoUserSelection', pad=([20,0],[0,0]))

headingLeftColumn = gui.Text('Auswahl: Anwendungsgebiet', background_color='#66bb6a', border_width=15, size=(37,1), justification='center', key='headingLeftColumn', pad=([81,0],[35,25]))

buttonPressed = 4

#evtl in window/layout rein
gui.SetOptions(background_color='#cee1cf',      
       use_ttk_buttons=True,
       button_color=('white', '#66bb6a'),
       text_color='black')

leftLeftColumn = [[buttonOne],[infoTextButtonOne]]
leftCenterColumn = [[buttonTwo], [infoTextButtonTwo]]
leftRightColumn = [[buttonThree], [infoTextButtonThree]]

leftColumn = [[headingLeftColumn], [gui.Column(leftLeftColumn), gui.Column(leftCenterColumn), gui.Column(leftRightColumn)],[buttonPrevious, buttonNext]]
rightColumn = [[infoTextRowNamesUserSelection, infoTextCurrentUserSelection]]

layout = [[gui.Column(leftColumn, size=(600, 600)), gui.VerticalSeparator(), gui.Column(rightColumn, size=(400, 600))]]

window = gui.Window('PC Builder', layout, margins=(0,0), element_padding=(0,0), no_titlebar=False, grab_anywhere=False, use_default_focus=False, icon=imageData.buttonUsedForThree, font='Consolas', finalize=True)

#initialize, später löschen
viewController.updatePageAndElementsOnNextButtonClick(4, window)     

while True:            
    event, values = window.read()
    
    if event == gui.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'buttonOne':
        buttonPressed = 1
    elif event == 'buttonTwo':
        buttonPressed = 2
    elif event == 'buttonThree':
        buttonPressed = 3
    elif event == 'buttonNext':
        viewController.updatePageAndElementsOnNextButtonClick(buttonPressed, window)        
        buttonPressed = 4
    elif event == 'buttonPrevious':
        viewController.updatePageAndElementsOnPreviousButtonClick(buttonPressed, window)        
        buttonPressed = 4 

window.close()