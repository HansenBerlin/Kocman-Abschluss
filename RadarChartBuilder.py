import plotly.graph_objects as go
import os

categories = ['Rechenleistung', 'Grafikleistung', 'Akku', 'Speicher', 'Robustheit', 'Lautstärke', 'Gewicht', 'Preis']  

class RadarChartBuilder(object):
    def __init__(self):        
        self.createDirectory()
        print(self.categories)
        categories = self.categories.reverse()
        print(categories)

        
    def createDirectory(self):
        try: 
            if not os.path.exists("plotImages"): os.mkdir("plotImages")
        except: print('Konnte Pfad nicht erstellen. Bitte im selben Verzeichnis wie diese Dateien einen Ordner mit dem Namen plotImages erstellen.')
    
    
    def buildRadarChart(self):
        fig = go.Figure()     

        fig.add_trace(go.Barpolar(
            r=[1,1,1,1,1,1,1,1],
            theta=categories,
            marker_color='rgb(71, 75, 205)',
            marker_line_color="black",
            marker_line_width=1,
            opacity=0.8
        ))
        fig.add_trace(go.Barpolar(
            r=[1,1,1,1,1,1,1,0],
            theta=categories,
            marker_color='rgb(0, 116, 231)',
            marker_line_color="black",
            marker_line_width=1,
            opacity=0.8
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,1,1,0,1,1,1,0],
            theta=categories,
            marker_color='rgb(0, 143, 220)',
            marker_line_color="black",
            marker_line_width=1,
            opacity=0.8
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,1,1,0,0,1,1,0],
            theta=categories,
            marker_color='rgb(0, 163, 183)',
            marker_line_color="black",
            marker_line_width=1,
            opacity=0.8
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,0,1,0,1,0,1,0],
            theta=categories,
            marker_color='rgb(0, 177, 139)',
            marker_line_color="black",
            marker_line_width=1,
            opacity=0.8
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,0,0,0,1,0,0,0],
            theta=categories,
            marker_color='rgb(102, 187, 106)',
            marker_line_color="black",
            marker_line_width=1,
            opacity=0.8
        ))       
        
        fig.update_traces()
        fig.update_layout(
            template="none",
            margin=dict(r=0, t=30, b=30, l=0),
            font_size=12,
            legend_font_size=14,
            font_family='Consolas',
            showlegend = False,
            font_color='#000000',
            polar = dict(bgcolor='#eef5ef', radialaxis = dict(visible = False, range = [0, 6]), angularaxis = dict(rotation=-45)),
            paper_bgcolor='#eef5ef'            
        )

        #fig.write_image("plotImages/radarplotUserSelection7.png", 'png', 'kaleido', width=500, height=400)

    