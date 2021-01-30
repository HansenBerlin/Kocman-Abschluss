from ImageDataModel import ImageData
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_CLOSES_WIN
import time
import sys

imageData = ImageData() 

'''Aufruf des Bestätigungsfensters wenn auf Kaufen geklickt wurde. Hier werden nochmal die Leistungswerte zusammengefasst
und fließen in unterschiedlicher Gewichtung in den benchmark mit ein. Vergleichswert ist der maximal mögliche Wert bei diesen
Konfigurationsmöglichkeiten (54, entspricht hier 100)'''

def createView(indexPoints, price, lastWindow):
    lastWindow.close()

    buttonConfirm = gui.Button('', image_data=imageData.buttonCloseWindow, pad=([165,10],[20,40]), button_type=BUTTON_TYPE_CLOSES_WIN, size=(14,1), key='btnConfirmAndFinish', button_color=('white', '#66bb6a'))
    layout = [[gui.Text('', key='indexValue', pad=([175,30],[40,1]), background_color='#eef5ef', font='Consolas', size=(20,2), justification='center')],
                [gui.ProgressBar(100, orientation='h', size=(40, 30), key='progressbar', pad=(40,10))],
                [gui.Text('{}:\n{}€'.format('Preis', price), pad=([175,10],[10,1]), background_color='#eef5ef', font='Consolas', size=(20,2), justification='center')],
                [gui.Text('{}€\n{}'.format(round(price/indexPoints, 2), 'pro Benchmarkpunkt'), pad=([175,10],[10,1]), background_color='#eef5ef', font='Consolas', size=(20,2), justification='center')],
                [buttonConfirm],
                [gui.Image(filename='ressources/computerguy.png')]]

    window = gui.Window('VIELEN DANK UND VIEL SPASS MIT DEM NEUEN NOTEBOOK').Layout(layout)
    progress_bar = window.FindElement('progressbar')

    wait = round(1/indexPoints, 4)
    timeout = 0

    while True:            
        event, values = window.read(timeout=timeout)

        for i in range(indexPoints+1):
            time.sleep(wait)
            progress_bar.UpdateBar(i + 1)
            window['indexValue'].update('{}:\n{}/100'.format('Benchmark', i))
        timeout = 1000000
        if event == gui.WIN_CLOSED or event == 'Exit':
            sys.exit()
   

