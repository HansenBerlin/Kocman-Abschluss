import plotly.graph_objects as go

# Höherer Farbindex=bessere Leistung; cD = Colordictionary
cD = {     
        1: 'rgb(205, 71, 120)',
        2: 'rgb(173, 58, 162)',        
        3: 'rgb(71, 75, 205)',
        4: 'rgb(0, 116, 231)',
        5: 'rgb(0, 143, 220)',
        6: 'rgb(0, 163, 183)',
        7: 'rgb(0, 177, 139)',
        8: 'rgb(102, 187, 106)'        
        }

class RadarChartBuilderController(object):

    def __init__(self):
        self.categories = ['Rechenleistung', 'Preis', 'Gewicht', 'Lautstärke', 'Robustheit', 'Speicher', 'Akku', 'Grafikleistung']   


    '''Erstellen des Datensets aus den aktuellen Indexwerten. Ein zweidimensionaler Array wird aufgebaut, die Werte des 
    Arrays an Index 0 sind alle 1, damit im Graphen keine Nullwerte angezeigt werden. Danach werden die weiteren Arrays aufgebaut
    und spaltenweise mit Einsen befüllt solange der Wert des übergebenen Indexvalues an der jeweiligen Position noch größer oder
    gleich der Reihe des zu befüllenden Arrays ist'''
    def createDataSet(self, indexedValues):    
        for i in range(8):
            if indexedValues[i] < 1: indexedValues[i] = 1    
        dataSet=[[1,1,1,1,1,1,1,1],[],[],[],[],[],[],[]]
        for i in range(1,8):
            for j in range(8):
                if indexedValues[j] > i:
                    dataSet[i].append(1)
                else: dataSet[i].append(0)
        return dataSet



    
    '''Erstellen des Graphen durch einen Loop. Die Farben werden unterschiedlich gesetzt, je nachdem ob ein 
    hoher Wert gut oder schlecht ist. Anschließend wird der Graph in eine Bilddatei umgewandelt, weil der dynamische 
    Graph mit dieser UI-Bibliothek nicht ohne weiteres angezeigt werden kann.'''
    def buildRadarChart(self, dataSet):
        fig = go.Figure()
        j = 8
        for i in range(8):
            fig.add_trace(go.Barpolar(
                r = dataSet[i],
                theta = self.categories,
                marker_color = [cD[i+1],cD[j],cD[j],cD[j],cD[i+1],cD[i+1],cD[i+1],cD[i+1]],
                marker_line_color = "#181818",
                marker_line_width = 1,
                opacity = 0.9
            ))
            j-=1

        fig.update_traces()
        fig.update_layout(
            template = "none",
            margin = dict(r = 0, t = 30, b = 30, l = 0),
            font_size = 12,
            legend_font_size = 14,
            font_family = 'Consolas',
            showlegend = False,
            font_color = '#000000',
            polar = dict(bgcolor='#eef5ef', radialaxis = dict(visible = False, range = [0, 8]), angularaxis = dict(rotation=90)),
            paper_bgcolor='#eef5ef'            
        )
        fig.write_image("ressources/radarplotUserSelection.png", 'png', 'kaleido', width = 500, height = 400)
