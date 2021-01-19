
class AvailableOptionsModel(object):    

    def __init__(self):        
        self.price = ['maximaler Preis', ['günstig', 'moderat', 'hoch'], -1]
        self.category = ['Kategorie', ['Custom', 'Budget', 'Business', 'Gaming', 'Outdoor'], -1, [False, False, False, False, False]]
        self.allOptions = [self.price, self.category]   


    def printArray(self):
        arrayEntrysForDebugging = "{}".format(self.category[3][0]) + "{}".format(self.category[3][1]) + "{}".format(self.category[3][2]) + "{}".format(self.category[3][3]) + "{}".format(self.category[3][4])
        return arrayEntrysForDebugging

    

        

    

    