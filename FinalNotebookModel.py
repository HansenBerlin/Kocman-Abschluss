from AvailableOptionsModel import AvailableOptionsModel

class FinalNotebookModel:
    
    def __init__(self):

        self.finalConfig = AvailableOptionsModel.getSavedIndexValues()

        self.availableCaseDict = {
            1: 'Plastik',
            2: 'Plastik',
            3: 'Plastik',
            4: 'Aluminium & Plastik',
            5: 'Aluminium',
            6: 'Verbundstoff, Aluminium',
            7: 'Aluminium (Einblockguss)',
            8: 'Carbon'
        }

        self.availableProcessorsDict = {
            1: 'Intel Atom x5 2C 1.80GHz, 2 Core',
            2: 'Intel Atom x5 2C 1.80GHz, 2 Core',
            3: 'Intel Core i3-8109U 3.00GHz, 2 Core',
            4: 'AMD Ryzen 3 3300U, 2.10GHz, 4 Core',
            5: 'Intel Core i5-8400H 2.50GHz, 4 Core',
            6: 'Intel Core i7-9750H 2.60GHz, 6 Core',
            7: 'Intel Core i9-10980HK 2.40GHz, 8 Core',
            8: 'AMD Ryzen 9 5900HX, 3.30 GHz, 8 Core'
        }

        self.availableRamDict = {
            1: '4 GB DDR3 1866 MHz (eff.)',
            2: '4 GB DDR4 1866 MHz (eff.)',
            3: '8 GB DDR4 2133 MHz (eff.)',
            4: '8 GB DDR4 2400 MHz (eff.)',
            5: '16 GB DDR4 2400 MHz (eff.)',
            6: '16 GB DDR4 3200 MHz (eff.)',
            7: '32 GB DDR5 3200 MHz (eff.)',
            8: '48 GB DDR5 4000 MHz (eff.)'
        }

        self.availableStorageDict = {
            1: '250 GB HDD',
            2: '120 GB SSD',
            3: '200 GB SSD',
            4: '200 GB SSD, 500 GB HDD',
            5: '500 GB SSD',
            6: '500 GB SSD, 1 TB HDD',
            7: '1 TB SSD',
            8: '2 TB SSD'
        }

        self.availableGPUDict = {
            1: 'onboard',
            2: 'onboard',
            3: 'onboard',
            4: 'NVIDIA GeForce GTX 980M',
            5: 'NVIDIA GeForce RTX 2060 Mobile',
            6: 'AMD Radeon RX 6700M',
            7: 'NVIDIA GeForce GTX 1080 SLI ',
            8: 'GeForce RTX 3080 Laptop GPU'
        }

        self.availableGPUIfProfessionalDict = {
            1: 'onboard',
            2: 'onboard',
            3: 'onboard',
            4: 'NVIDIA GeForce GTX 980M',
            5: 'NVIDIA GeForce RTX 2060 Mobile',
            6: 'AMD Radeon RX 6700M',
            7: 'NVIDIA Quadro RTX 5000',
            8: 'Quadro RTX 6000'
        }

        self.availableScreenDict = {
            1: '13 Zoll 720p',
            2: '13 Zoll 1080p',
            3: '14 Zoll 1080p',
            4: '14 Zoll 1080p',
            5: '15 Zoll 1080p',
            6: '16 Zoll 1080p',
            7: '16 Zoll 4K',
            8: '17 Zoll 4K'
        }

        self.availableBatteryDict = {
            1: 'Laufzeit (Durchschn.: 1 Std.)',
            2: 'Laufzeit (Durchschn.: 2 Std.)',
            3: 'Laufzeit (Durchschn.: 4 Std.)',
            4: 'Laufzeit (Durchschn.: 5 Std.)',
            5: 'Laufzeit (Durchschn.: 7 Std.)',
            6: 'Laufzeit (Durchschn.: 10 Std.)',
            7: 'Laufzeit (Durchschn.: 12 Std.)',
            8: 'Laufzeit (Durchschn.: >12 Std.)',       }        

        self.availableCoolerSystemDict = {
            1: 'passiv',
            2: 'passiv',
            3: 'passiv',
            4: '1 CPU Lüfter',
            5: '1 CPU Lüfter',
            6: '1 CPU Lüfter, 1 Gehäuselüfter',
            7: '1 CPU Lüfter, 1 Gehäuselüfter',
            8: '3 Lüfter'
        }

        self.pricesDict = {   
            1: 280,
            2: 450,
            3: 700,
            4: 900,
            5: 1600,
            6: 2300,
            7: 3200,
            8: 4600
        }

        self.dictionaryCollection = [self.availableProcessorsDict, self.pricesDict, self.availableScreenDict, 
                                    self.availableCoolerSystemDict, self.availableCaseDict, self.availableStorageDict, 
                                    self.availableBatteryDict, self.availableGPUDict, self.availableRamDict]

                                   
    def createConfigArray(self):
        finalConfigurationOnView = []
        for i in range(8):
            if self.finalConfig[i]<0: self.finalConfig[i] = 0
            elif self.finalConfig[i]>7: self.finalConfig[i] = 7
            if i == 1:
                if AvailableOptionsModel.getFinalConfigState()[5] == 'Business-Level':
                    finalConfigurationOnView.append(self.dictionaryCollection[i][self.finalConfig[i]+1]*1.2)
                elif AvailableOptionsModel.getFinalConfigState()[5] == 'Outdoor/Special':
                    finalConfigurationOnView.append(self.dictionaryCollection[i][self.finalConfig[i]+1]*1.5)
                else: finalConfigurationOnView.append(self.dictionaryCollection[i][self.finalConfig[i]+1])
            elif i == 7:
                if AvailableOptionsModel.getFinalConfigState()[0] == 'Professional':
                    finalConfigurationOnView.append(self.availableGPUIfProfessionalDict[self.finalConfig[i]+1])
                else: finalConfigurationOnView.append(self.dictionaryCollection[i][self.finalConfig[i]+1])
            else: finalConfigurationOnView.append(self.dictionaryCollection[i][self.finalConfig[i]+1])
        finalConfigurationOnView.append(self.dictionaryCollection[8][self.finalConfig[0]+1])

        return finalConfigurationOnView

        



       # self.categories = ['Rechenleistung', 'Preis', 'Gewicht', 'Lautstärke', 'Robustheit', 'Speicher', 'Akku', 'Grafikleistung']    


