from ViewController import ViewController
from AvailableOptionsModel import AvailableOptionsModel
from tkinter.constants import ACTIVE, DISABLED, FALSE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window


buttonNext = sg.Button('NEXT', image_size=(100, 50), image_subsample=4, border_width=10, key='buttonNext')
testModel = AvailableOptionsModel()
viewController = ViewController()

buttonPressed = 0




theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

leftColumn = [[sg.Text('Preis moderat', font='Any 12', key='textblockFour')],
            [viewController.buttonOne],
            [sg.Text('Preis güntig', font='Any 12', key='textblockFour')],
            [viewController.buttonTwo],
            ]

rightColumn = [[sg.Text(testModel.category[3], font='Any 10', key='debugOptions')],
            [buttonNext]            
            ]

layout = [[sg.Column(leftColumn, size=(300, 600), pad=BPAD_LEFT, key="testtest")],
        [sg.Column(rightColumn, size=(600,600), pad=BPAD_RIGHT)]
        ]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=True)

while True:             # Event Loop
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'buttonOne':
        buttonPressed = 1
        testModel.changeSelection('price', 0)
        #window['debugOptions'].update(testModel.printArray())
    elif event == 'buttonTwo':
        buttonPressed = 2
        testModel.changeSelection('price', 1)
        #window['debugOptions'].update(testModel.printArray())
    elif event == 'buttonNext':
        viewController.clickNextButton(buttonPressed)
        window['buttonOne'].update(image_data=viewController.updateButtonIcon(1))
        window['buttonTwo'].update(image_data=viewController.updateButtonIcon(2))
        window['buttonOne'].update(disabled=viewController.updateOptions(1))
        window['buttonTwo'].update(disabled=viewController.updateOptions(2))       

window.close()