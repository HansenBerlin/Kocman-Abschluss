from ViewController import ViewController
from AvailableOptionsModel import AvailableOptionsModel
from ImageData import ImageData
import PySimpleGUI as gui

buttonNext = gui.Button('NEXT', size=(30,5), border_width=2, key='buttonNext')
testModel = AvailableOptionsModel()
viewController = ViewController()

imageData = ImageData()     
buttonOne = gui.Button('', image_data=imageData.price, border_width=2, key='buttonOne')
buttonTwo = gui.Button('', image_data=imageData.price, border_width=2, key='buttonTwo')
buttonThree = gui.Button('', image_data=imageData.price, border_width=2, key='buttonThree')

headerTextButtonOne = gui.Text('Preis günstig', font='Fixedsys 12', key='textAboveButtonOne')
headerTextButtonTwo = gui.Text('Preis moderat', font='Fixedsys 12', key='textAboveButtonTwo')
headerTextButtonThree = gui.Text('Preis egal', font='Fixedsys 12', key='textAboveButtonThree')

infoTextButtonOne = gui.Text('Info1', font='Fixedsys 12', key='textInfoButtonOne')
infoTextButtonTwo = gui.Text('Info2', font='Fixedsys 12', key='textInfoButtonTwo')
infoTextButtonThree = gui.Text('Info3', font='Fixedsys 12', key='textInfoButtonThree')

buttonPressed = 0

gui.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

leftLeftColumn = [[headerTextButtonOne],[buttonOne],[infoTextButtonOne]]
leftCenterColumn = [[headerTextButtonTwo], [buttonTwo], [infoTextButtonTwo]]
leftRightColumn = [[headerTextButtonThree], [buttonThree], [infoTextButtonThree]]

leftColumn = [[gui.Column(leftLeftColumn), gui.Column(leftCenterColumn), gui.Column(leftRightColumn)],[buttonNext]]
rightColumn = [[gui.Text(testModel.category[3], font='Any 10', key='debugOptions')]]

layout = [[gui.Column(leftColumn, size=(600, 600)), gui.Column(rightColumn, size=(400, 600))]]

window = gui.Window('Dashboard PySimpleGUI-Style', layout, margins=(5,5), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)

while True:            
    event, values = window.read()
    
    if event == gui.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'buttonOne':
        buttonPressed = 1
    elif event == 'buttonTwo':
        buttonPressed = 2
    elif event == 'buttonTwo':
        buttonPressed = 2
    elif event == 'buttonNext':
        viewController.clickNextButton(buttonPressed)
        window['buttonOne'].update(image_data=viewController.updateButtonIcon(1))
        window['buttonTwo'].update(image_data=viewController.updateButtonIcon(2))
        window['buttonThree'].update(image_data=viewController.updateButtonIcon(3))
        window['buttonOne'].update(disabled=viewController.updateOptions(1))
        window['buttonTwo'].update(disabled=viewController.updateOptions(2))      
        window['buttonThree'].update(disabled=viewController.updateOptions(3))   

window.close()