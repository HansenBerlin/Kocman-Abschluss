from UserSelectionView import UserSelectionView

try: 
    UserSelectionView.initMainWindow()
except: 
    print('Das Programm konnte nicht geladen werden, wahrscheinlich fehlen Abhängigkeiten.\n' +
    'Diese sollten eigentlich über dieses programm installiert werden, das hat nicht geklappt :-(\n'+
    'Folgende Bibliotheken müssen manuell installiert werden (mit Befehl zur Installation via PowerShell:\n'+
    'PySimpleGUI        <pip install PySimpleGUI>\n'+
    'Plotly Express     <pip install plotly-express>\n'+
    'Kaleido            <pip install kaleido>\n'+
    'Pandas             <pip install pandas>'
    )

