from UserSelectionView import UserSelectionView
import subprocess
import sys

'''Programmaufbau siehe beiliegende Dokumentation, die wichtigsten 
Funktionen sind zusätzlich im Code dokumentiert
Repo: https://github.com/HansenBerlin/Kocman-Abschluss'''

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

dependencies = ['PySimpleGUI', 'plotly-express', 'kaleido', 'pandas']


userInput = input('++++++++++++++++++++++++++++++++++++++++++++++++++++\n'+
                'Möchtest du notwendige Abhängigkeiten installieren?\n'+
                'ENTER drücken zum überspringen\n'+
                'y und mit ENTER bestätigen zum installieren')
if userInput == 'y':
    try: 
        for i in dependencies:
            install(i)
    except: 
        print('Das Programm konnte nicht geladen werden, wahrscheinlich fehlen Abhängigkeiten.\n' +
        'Diese sollten eigentlich über dieses Programm installiert werden, das hat nicht geklappt :-(\n'+
        'Folgende Bibliotheken müssen manuell installiert werden (mit Befehl zur Installation via PowerShell:\n'+
        'PySimpleGUI        <pip install PySimpleGUI>\n'+
        'Plotly Express     <pip install plotly-express>\n'+
        'Kaleido            <pip install kaleido>\n'+
        'Pandas             <pip install pandas>')

try:
    print('Starte Hauptprogramm...')
    UserSelectionView.initMainWindow()
except Exception as e:
    print(e)

