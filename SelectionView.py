from tkinter.constants import ACTIVE, FALSE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
  



block_3 = [[sg.Text('Block 3', font='Any 20')],
            [sg.Input(), sg.Text('Some Text')],
            [sg.Button('Go'), sg.Button('Exit')]  ]


block_2 = [[sg.Text('Block 2', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.Image(data=sg.DEFAULT_BASE64_ICON)]  ]

block_4 = [[sg.Text('Block 4', font='Any 20', key='textblockFour')],
            [priceComboBox],
            [processorComboBox],
            #[sg.T('This is some random text')],
            #[sg.T('This is some random text')]
            ]





