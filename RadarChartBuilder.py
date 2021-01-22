from typing import Text
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

class RadarChartBuilder(object):
    def __init__(self):
        self.buildChart()
        self.buildChart2()

        #img_bytes = fig.to_image(format="png")


    def buildChart(self):
        df = pd.DataFrame(dict(
            r=[75, 100, 75, 100, 75, 100, 75, 100],
            theta = ['Rechenleistung', 'Grafikleistung', 'Speicherplatz', 'Akkulaufzeit', 'Preis', 'Robustheit', 'Gewicht', 'Lautstärke'])) 

        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself')
        fig.update_layout(
            template="plotly_dark",
            margin=dict(r=0, t=20, b=20, l=0),
            font_size=10,
            legend_font_size=14,
            showlegend = False)

        if not os.path.exists("images"):
            os.mkdir("images")

        #fig.show()
        fig.write_image("images/fig1.png", 'png', 'kaleido')
        #image_hex = px.image.get(fig, format='png', height=fig['layout']['height'], width=fig['layout']['width'])
        #return image_hex
        

    def buildChart2(self):
        df = px.data.wind()        
        fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark", color_discrete_sequence= px.colors.sequential.Plasma_r)
        fig.write_image("images/fig2.png", 'png', 'kaleido')

    
    
    def buildChart3(self):
        categories = ['Preis', 'Grafikleistung', 'Rechenleistung', 'Akkulaufzeit', 'Gewicht', 'Robustheit', 'Speicherplatz', 'Lautstärke']  
        fig = go.Figure()

        fig.add_trace(go.Barpolar(
            r=[1,1,1,1,1,1,1,1],
            name='niedrig',
            theta=categories,
            marker_color='rgb(71, 75, 205)'
        ))
        fig.add_trace(go.Barpolar(
            r=[1,1,1,1,1,1,1,0],
            name='niedrig',
            theta=categories,
            marker_color='rgb(0, 116, 231)'
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,1,1,0,1,1,1,0],
            name='niedrig',
            theta=categories,
            marker_color='rgb(0, 143, 220)'
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,1,1,0,0,1,1,0],
            name='niedrig',
            theta=categories,
            marker_color='rgb(0, 163, 183)'
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,0,1,0,1,0,1,0],
            name='niedrig',
            theta=categories,
            marker_color='rgb(0, 177, 139)'
        ))  
        fig.add_trace(go.Barpolar(
            r=[1,0,0,0,1,0,0,0],
            name='niedrig',
            theta=categories,
            marker_color='rgb(102, 187, 106)'
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
            polar = dict(bgcolor='#cee1cf'),
            paper_bgcolor='#cee1cf'
            
        )

        fig.write_image("images/fig3.png", 'png', 'kaleido', width=500, height=400)

    