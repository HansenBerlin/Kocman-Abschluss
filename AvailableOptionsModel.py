savedConfigFinalState = []
savedIndexValues = []

class AvailableOptionsModel(object):   

    def setFinalConfigState(config, parts):
        global savedConfigFinalState
        global savedIndexValues
        savedConfigFinalState = config
        savedIndexValues = parts

    def getFinalConfigState():
        return savedConfigFinalState

    def getSavedIndexValues():
        return savedIndexValues


    def __init__(self):  

        self.category = ['Gesamtleistung/Anwendungsgebiet', 
                        ['Office: \n \n•Officeanwendungen \n•Internetnutzung \n•Webdesign \n \n', 
                        'Gaming: \n \n•wie Office plus: \n•Gaming (inkl. VR) \n•Bild- und \n Videobearbeitung \n', 
                        'Professional: \n \n•Entwicklung \n•Machine Learning \n•Workstation \n•Bild- und \n Videobearbeitung'],
                         4, [False, False, False, False]]     

        self.price =    ['maximaler Preis', 
                        ['niedrig: \n \n•einige Ein- \n schränkungen \n in der weiteren \n Auswahl  \n', 
                        'mittel: \n \n•ausreichend \n für die meisten \n Konfigurationen \n \n', 
                        'hoch: \n \n•keine Ein- \n schränkungen \n der weiteren \n Optionen \n'],
                        4, [False, False, False, False]]

        self.sizeAndWeight = ['Größe und Gewicht', 
                        ['klein & leicht: \n \n•max 13 Zoll \n•max 1200g \n•kein Numpad \n•nicht erweiterbar \n', 
                        'mittel: \n \n•14-15 Zoll \n•max 2000g \n•externes Netzteil \n•erweiterbar \n', 
                        'groß: \n \n•Desktopersatz \n•relativ laut \n•ermöglicht leis- \n tungsstarke \n Konfiguration'],
                         4, [False, False, False, False]]     

        self.batteryLife =    ['Akkulaufzeit', 
                        ['niedrig: \n \n•min. 2 Std. \n \n \n \n', 
                        'mittel: \n \n•min. 4 Std \n•max 8 Std. \n \n \n', 
                        'lang: \n \n•>8 Std. \n \n \n \n'],
                        4, [False, False, False, False]]

        self.noiseEmission =    ['Lautstärkeentwicklung', 
                        ['laut: \n \n•lauter Lüfter \n•max. moderate \n Hitzeentwicklung \n \n', 
                        'moderat: \n \n•Lüfter nur bei \n hoher Last \n•moderate Hitze- \n entwicklung \n', 
                        'flüsterleise: \n \n•kein Lüfter \n•nicht für kleine Ge- \n häuse möglich \n•ggfs. hohe Hitze- \n entwicklung'],
                        4, [False, False, False, False]]

        self.durability =    ['Robustheit', 
                        ['Consumer: \n \n•bewährte All- \n tagsqualität \n•Garantie 2 Jahre \n•max. 5 Pixelfehler \n', 
                        'Business-Level: \n \n•hohe Robustheit \n für tägl. Einsatz \n•Garantie 3 Jahre \n•Spritzwasserschutz \n•keine Pixelfehler', 
                        'Outdoor/Special: \n \n•maximale Robustheit \n•für Außeneinsätze \n (Baustelle) geeignet \n•Garantie 5 Jahre \n•IP68 zertifiziert'],
                        4, [False, False, False, False]]


        self.allOptions = [self.category, self.price, self.sizeAndWeight, self.batteryLife, self.noiseEmission, self.durability]

        self.partIndexValues = [3,3,3,3,3,3,3,3]        
        self.savedConfigurations = []
        self.savedButtonChoices = [4,4,4,4,4,4]

        self.userSelection = {
            1: ['Office', 'Gaming', 'Professional', 'keine Präferenz'],
            2: ['niedrig', 'mittel', 'hoch', 'keine Präferenz'],
            3: ['klein & leicht', 'mittel', 'groß', 'keine Präferenz'],
            4: ['niedrig ', 'mittel', 'lang', 'keine Präferenz'],
            5: ['laut', 'moderat', 'flüsterleise', 'keine Präferenz'],
            6: ['Consumer', 'Business-Level', 'Outdoor/Special', 'keine Präferenz']            
        }

        

        
           

    

    

        

    

    