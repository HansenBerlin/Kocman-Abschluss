from ImageDataModel import ImageData
import PySimpleGUI as sg
import time

from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_CLOSES_WIN
imageData = ImageData() 


buttonConfirm = sg.Button('', image_data=imageData.buttonDone, pad=([165,10],[20,40]), button_type=BUTTON_TYPE_CLOSES_WIN, size=(14,1), key='btnConfirmAndFinish', button_color=('white', '#66bb6a'))
indexPoints = 100
price = 4560

layout = [[sg.Text('', key='indexValue', pad=([175,30],[40,1]), font='Consolas', size=(20,2), justification='center')],
            [sg.ProgressBar(200, orientation='h', size=(40, 30), key='progressbar', pad=(40,10))],
            [sg.Text('{}:\n{}€'.format('Preis', price), pad=([175,10],[10,1]), font='Consolas', size=(20,2), justification='center')],
            [sg.Text('{}:\n{}'.format('Leistungspunkte/€', round(price/indexPoints, 2)), pad=([175,10],[10,1]), font='Consolas', size=(20,2), justification='center')],
            [buttonConfirm]]

window = sg.Window('VIELEN DANK').Layout(layout)
progress_bar = window.FindElement('progressbar')

wait = round(2/indexPoints, 2)
timeout = 0

while True:            
    event, values = window.read(timeout=timeout)

    for i in range(indexPoints+1):
        time.sleep(wait)
        progress_bar.UpdateBar(i + 1)
        window['indexValue'].update('{}:\n{}/200'.format('Leistungsindex', i))
    timeout = 1000000
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.Close()

