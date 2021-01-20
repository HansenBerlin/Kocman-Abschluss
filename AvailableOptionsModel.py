
class AvailableOptionsModel(object):    

    def __init__(self):  

        self.category = ['Auswahl: Anwendungsgebiet', 
                        ['Office: \n \nOfficeenwendungen \nInternetnutzung \nWebdesign \n \n', 
                        'Gaming: \n \nwie Office plus: \nGaming \nVR \nBild- und \nVideobearbeitung', 
                        'Professional: \n \nEntwicklung \nMachine Learning \nWorkstation \nBild- und \nVideobearbeitung'],
                         -1, [False, False, False]]     

        self.price =    ['Auswahl: maximaler Preis', 
                        ['niedrig: \n \neinige Ein- \nschränkungen \nin der weiteren \nAuswahl  \n', 
                        'mittel: \n \nausreichend \nfür die meisten \nKonfigurationen \n \n', 
                        'hoch/egal: \n \nkeine Ein- \nschränkungen \nder weiteren \nOptionen \n'],
                        -1, [False, False, False]]

        self.sizeAndWeight = ['Auswahl: Größe und Gewicht', 
                        ['klein & leicht: \n \nmax 13 Zoll \nmax 1200g \nkein Numpad \nnicht erweiterbar \n', 
                        'mittel: \n \n14-15 Zoll \nmax 2000g \nexternes Netzteil \nerweiterbar \n', 
                        'groß/egal: \n \nDesktopersatz \nrelativ laut \nermöglicht leis- \ntungsstarke \nKonfiguration'],
                         -1, [False, False, False]]     

        self.batteryLife =    ['Auswahl: Akkulaufzeit', 
                        ['niedrig/egal: \n \nmin. 2 Std. \n \n \n \n', 
                        'mittel: \n \nmin. 4 Std \nmax 8 Std. \n \n \n', 
                        'lang: \n \n>8 Std. \n \n \n \n'],
                        -1, [False, False, False]]

        self.noiseEmission =    ['Auswahl: Lautstärkeentwicklung', 
                        ['niedrig/egal: \n \nmin. 2 Std. \n \n \n \n', 
                        'mittel: \n \nmin. 4 Std \nmax 8 Std. \n \n \n', 
                        'lang: \n \n>8 Std. \n \n \n \n'],
                        -1, [False, False, False]]

        self.durability =    ['Auswahl: Robustheit', 
                        ['niedrig/egal: \n \nmin. 2 Std. \n \n \n \n', 
                        'mittel: \n \nmin. 4 Std \nmax 8 Std. \n \n \n', 
                        'lang: \n \n>8 Std. \n \n \n \n'],
                        -1, [False, False, False]]


        self.allOptions = [self.category, self.price, self.sizeAndWeight, self.batteryLife, self.noiseEmission, self.durability]

        # Dictionary um für jede Runde die Zwischenkonfiguration zu speichern
        # wird nur benötigt, wenn der Nutzer zurückgeht um die Werte der nachfolgenden
        # Runden zurückzusetzen
        
        self.savedConfigurations = []
        for i in range(6):
            self.savedConfigurations.append(self.allOptions)     

    

    

        

    

    