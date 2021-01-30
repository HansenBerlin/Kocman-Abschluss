from ViewController import ViewController
from ImageDataModel import ImageData
import PySimpleGUI as gui


class FinalNotebookView():

    def initMainWindow(exitProgram):
        if exitProgram: return -1

        fileNameImageDict= {
                        0: 'ressources/parts (1).png',
                        1: 'ressources/parts (7).png',
                        2: 'ressources/parts (6).png',
                        3: 'ressources/parts (4).png',
                        4: 'ressources/parts (2).png',
                        5: 'ressources/parts (9).png',
                        6: 'ressources/parts (3).png',
                        7: 'ressources/parts (5).png',
                        8: 'ressources/parts (8).png'
        }

        headingTextDict= {
                        0: 'Gehäuse',
                        1: 'Prozessor',
                        2: 'Arbeitsspeicher',
                        3: 'Festplatte',
                        4: 'Grafikkarte',
                        5: 'Bildschirm',
                        6: 'Akku',
                        7: 'Lüftersystem',
                        8: 'Preis'
        }

        infoTextKeysDict= {
                        0: 'keyCase',
                        1: 'keyProzessor',
                        2: 'keyArbeitsspeicher',
                        3: 'keyFestplatte',
                        4: 'keyGrafikkarte',
                        5: 'keyBildschirm',
                        6: 'keyAkku',
                        7: 'keyLüftersystem',
                        8: 'keyPreis'
        }

        imageData = ImageData() 
        viewController = ViewController()
       
        buttonConfirm = gui.Button('FERTIG', image_data=imageData.buttonConfirmPurchase, pad=([74,0],[10,0]), size=(1,1), key='btnConfirmAndFinish', button_color=('white', '#66bb6a'))
        infoTextRowNamesUserSelection = gui.Text('Anwendung/Leistung \nPreis \nGewicht und Größe \nAkkulaufzeit \nLautstärke \nRobustheit \n',font='Consolas 10', background_color='#eef5ef', text_color='black', pad=([80,0],[0,0]))
        infoTextCurrentUserSelection =   gui.Text('                                                                                          \n \n \n \n \n \n', font='Consolas 10', background_color='#eef5ef', text_color='black', key='textRightColumnInfoFinalSelection', pad=([20,0],[0,0]))
        headingLeftColumn = gui.Text('Ihre optimale Konfiguration', background_color='#252525', text_color='white', border_width=15, size=(45,1), justification='center', key='headingLeftColumn', pad=([81,0],[35,25]))
        headingRightColumn = gui.Text('Leistungsindex', text_color='white', background_color='#252525', border_width=15, size=(33,1), justification='center', pad=([81,0],[35,25]))
        plotCanvas = gui.Image(key='plotCanvas', pad=([0,0],[20,0]), size=(500,400), background_color='#eef5ef', filename='ressources/radarplotUserSelection.png')      

        colLeft = []      
        for i in range(9): colLeft.append([gui.Image(pad=([80,0],[4,4]), size=(32,32), background_color='#eef5ef', filename=fileNameImageDict[i])])

        colCenter = []      
        for i in range(9): colCenter.append([gui.Text(headingTextDict[i], pad=([20,0],[12,11]), font='Consolas 10', background_color='#eef5ef', text_color='black')])   

        colRight = []      
        for i in range(9): colRight.append([gui.Text('                                                        ', pad=([20,0],[12,11]), 
                            font='Consolas 10', background_color='#eef5ef', text_color='black', key=infoTextKeysDict[i])])       
        
        leftColumn = [[headingLeftColumn], [gui.Column(colLeft, background_color='#eef5ef'), 
                    gui.Column(colCenter, background_color='#eef5ef'), 
                    gui.Column(colRight, background_color='#eef5ef')],[buttonConfirm]]

        #evtl in window/layout rein
        gui.SetOptions(background_color='#eef5ef',      
               use_ttk_buttons=True,
               button_color=('white', '#66bb6a'),
               text_color='black')

        rightColumn = [[gui.Column([[headingRightColumn],[infoTextRowNamesUserSelection, infoTextCurrentUserSelection],[plotCanvas]])]]
        layout = [[gui.Column(leftColumn, size=(600, 700)), gui.VerticalSeparator(), gui.Column(rightColumn, size=(500, 700))]]
        window = gui.Window('Notebook-Builder for Noobs', layout, margins=(0,0), element_padding=(0,0), no_titlebar=False, grab_anywhere=False, 
                use_default_focus=False, icon=imageData.iconMainWindow, font='Consolas', finalize=True)
        
        viewController.updateComponentsInFinalView(window, infoTextKeysDict)

        while True:            
            event, values = window.read()

            if event == gui.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'btnConfirmAndFinish':
                gui.ProgressBar('Title', 0, 100, '_M_', 'This is my meter that will go to 100')


        window.close()