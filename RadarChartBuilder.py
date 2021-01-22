import plotly.graph_objects as go
import os

# Höherer Farbindex=bessere Leistung; cD = Colordictionary
cD = {        
        1: 'rgb(71, 75, 205)',
        2: 'rgb(0, 116, 231)',
        3:'rgb(0, 143, 220)',
        4: 'rgb(0, 163, 183)',
        5: 'rgb(0, 177, 139)',
        6: 'rgb(102, 187, 106)'  
        }

class RadarChartBuilder(object):

    def __init__(self):
        self.categories = ['Rechenleistung', 'Preis', 'Gewicht', 'Lautstärke', 'Robustheit', 'Speicher', 'Akku', 'Grafikleistung']    
    


    def createDataSet(self, indexedValues):
        #Werte unter 1 und über 6 bereinigen (kann in Extremfällen passieren)
        print(indexedValues)
        for i in range(8):
            if indexedValues[i] < 1: indexedValues[i] = 1
            elif indexedValues[i] > 6: indexedValues[i] = 6
        print(indexedValues)
        dataSet=[[],[],[],[],[],[]]
        for i in range(6):
            for j in range(8):
                if indexedValues[j] > i:
                    dataSet[i].append(1)
                else: dataSet[i].append(0)
        return dataSet


    def createDirectory(self):
        try: 
            if not os.path.exists("plotImages"): os.mkdir("plotImages")
        except: print('Konnte Pfad nicht erstellen. Bitte im selben Verzeichnis wie diese Dateien einen Ordner mit dem Namen plotImages erstellen.')
    
    
    def buildRadarChart(self, dataSet):
        fig = go.Figure()     
        fig.add_trace(go.Barpolar(
            r = dataSet[0],
            theta = self.categories,
            marker_color = [cD[1],cD[6],cD[6],cD[6],cD[1],cD[1],cD[1],cD[1]],
            marker_line_color = "black",
            marker_line_width = 1,
            opacity = 0.8
        ))
        fig.add_trace(go.Barpolar(
            r = dataSet[1],            
            theta = self.categories,
            marker_color = [cD[2],cD[5],cD[5],cD[5],cD[2],cD[2],cD[2],cD[2]],
            marker_line_color = "black",
            marker_line_width = 1,
            opacity = 0.8
        ))  
        fig.add_trace(go.Barpolar(
            r = dataSet[2],            
            theta = self.categories,
            marker_color = [cD[3],cD[4],cD[4],cD[4],cD[3],cD[3],cD[3],cD[3]],
            marker_line_color = "black",
            marker_line_width = 1,
            opacity = 0.8
        ))  
        fig.add_trace(go.Barpolar(
            r = dataSet[3],            
            theta = self.categories,
            marker_color = [cD[4],cD[3],cD[3],cD[3],cD[4],cD[4],cD[4],cD[4]],
            marker_line_color = "black",
            marker_line_width = 1,
            opacity = 0.8
        ))  
        fig.add_trace(go.Barpolar(
            r = dataSet[4],            
            theta=self.categories,
            marker_color = [cD[5],cD[2],cD[2],cD[2],cD[5],cD[5],cD[5],cD[5]],
            marker_line_color = "black",
            marker_line_width = 1,
            opacity = 0.8
        ))  
        fig.add_trace(go.Barpolar(
            r = dataSet[5],           
            theta = self.categories,
            marker_color = [cD[6],cD[1],cD[1],cD[1],cD[6],cD[6],cD[6],cD[6]],
            marker_line_color = "black",
            marker_line_width = 1,
            opacity = 0.8
        ))       

        fig.update_traces()
        fig.update_layout(
            template = "none",
            margin = dict(r = 0, t = 30, b = 30, l = 0),
            font_size = 12,
            legend_font_size = 14,
            font_family = 'Consolas',
            showlegend = False,
            font_color = '#000000',
            polar = dict(bgcolor='#eef5ef', radialaxis = dict(visible = False, range = [0, 6]), angularaxis = dict(rotation=90)),
            paper_bgcolor='#eef5ef'            
        )
        fig.write_image("plotImages/radarplotUserSelection4.png", 'png', 'kaleido', width = 500, height = 400)

    