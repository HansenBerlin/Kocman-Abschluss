from ImageDataModel import ImageData
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_CLOSES_WIN
import time
import sys

imageData = ImageData() 

def createView(indexPoints, price, lastWindow):
    lastWindow.close()
    buttonConfirm = gui.Button('', image_data=imageData.buttonCloseWindow, pad=([165,10],[20,40]), button_type=BUTTON_TYPE_CLOSES_WIN, size=(14,1), key='btnConfirmAndFinish', button_color=('white', '#66bb6a'))
    

    layout = [[gui.Text('', key='indexValue', pad=([175,30],[40,1]), font='Consolas', size=(20,2), justification='center')],
                [gui.ProgressBar(100, orientation='h', size=(40, 30), key='progressbar', pad=(40,10))],
                [gui.Text('{}:\n{}€'.format('Preis', price), pad=([175,10],[10,1]), font='Consolas', size=(20,2), justification='center')],
                [gui.Text('{}€\n{}'.format(round(price/indexPoints, 2), 'pro Leistungspunkt'), pad=([175,10],[10,1]), font='Consolas', size=(20,2), justification='center')],
                [buttonConfirm]]

    window = gui.Window('VIELEN DANK').Layout(layout)
    progress_bar = window.FindElement('progressbar')

    wait = round(1/indexPoints, 4)
    timeout = 0

    while True:            
        event, values = window.read(timeout=timeout)

        for i in range(indexPoints+1):
            time.sleep(wait)
            progress_bar.UpdateBar(i + 1)
            window['indexValue'].update('{}:\n{}%'.format('Leistungsindex', i))
        timeout = 1000000
        if event == gui.WIN_CLOSED or event == 'Exit':
            sys.exit()
   

