from PySimpleGUI.PySimpleGUI import Image
from ViewController import ViewController
from ImageData import ImageData
import PySimpleGUI as gui

class MainViewTwo():
    def initMainWindow():
        viewController = ViewController()
        imageData = ImageData() 
        #figTest = RadarChartBuilder() 

       
        buttonConfirm = gui.Button('FERTIG', image_data=imageData.buttonConfirmPurchase, pad=([74,0],[10,0]), size=(1,1), key='btnConfirmAndFinish', button_color=('white', '#66bb6a'))
       
        infoTextButtonOne =   gui.Text('  \n \n \n \n \n \n', font='Consolas 8', background_color='#eef5ef', text_color='black', key='textInfoButtonOne', pad=([81,0],[20,50]))
        infoTextButtonTwo =   gui.Text('    \n \n \n \n \n \n', font='Consolas 8', background_color='#eef5ef', text_color='black', key='textInfoButtonTwo', pad=([0,26],[20,50]))
        infoTextButtonThree =   gui.Text('     \n \n \n \n \n \n', font='Consolas 8', background_color='#eef5ef', text_color='black', key='textInfoButtonThree', pad=([0,0],[20,50]))
        infoTextRowNamesUserSelection = gui.Text('Anwendung/Leistung \nPreis \nGewicht und Größe \nAkkulaufzeit \nLautstärke \nRobustheit \n',font='Consolas 10', background_color='#eef5ef', text_color='black', pad=([80,0],[0,0]))
        infoTextCurrentUserSelection =   gui.Text('                                                                                          \n \n \n \n \n \n', font='Consolas 10', background_color='#eef5ef', text_color='black', key='textRightColumnInfoSelection', pad=([20,0],[0,0]))
        headingLeftColumn = gui.Text('Auswahl: Anwendungsgebiet', background_color='#252525', border_width=15, size=(45,1), justification='center', key='headingLeftColumn', pad=([81,0],[35,25]))
        headingRightColumn = gui.Text('Aktuelle Auswahl', background_color='#252525', border_width=15, size=(33,1), justification='center', pad=([81,0],[35,25]))
        plotCanvas = gui.Image(key='plotCanvas', pad=([0,0],[20,0]), size=(500,400), background_color='#eef5ef')    
        partsOverview = gui.Image(pad=([74,0],[10,0]), size=(450,400), background_color='#eef5ef', filename='ressources/secondScreenBg.png')    


        buttonPressed = 4

        #evtl in window/layout rein
        gui.SetOptions(background_color='#eef5ef',      
               use_ttk_buttons=True,
               button_color=('white', '#66bb6a'),
               text_color='black')

       
        leftColumn = [[headingLeftColumn], [partsOverview],[buttonConfirm]]
        rightColumn = [[gui.Column([[headingRightColumn],[infoTextRowNamesUserSelection, infoTextCurrentUserSelection],[plotCanvas]])]]
        layout = [[gui.Column(leftColumn, size=(600, 700)), gui.VerticalSeparator(), gui.Column(rightColumn, size=(500, 700))]]
        window = gui.Window('PC Builder', layout, margins=(0,0), element_padding=(0,0), no_titlebar=False, grab_anywhere=False, use_default_focus=False, icon=imageData.buttonUsedForThree, font='Consolas', finalize=True)

        viewController.updatePlotOnCanvas(buttonPressed, window) 
        viewController.updateRightColumnElements(buttonPressed, window)
        

        while True:            
            event, values = window.read()

            if event == gui.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'buttonOne':
                buttonPressed = 1  

        window.close()