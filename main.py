import subprocess
import sys

'''Programmaufbau siehe beiliegende Dokumentation, die wichtigsten 
Funktionen sind zusätzlich im Code dokumentiert
Repo: https://github.com/HansenBerlin/Kocman-Abschluss'''

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, '--user'])

dependencies = ['PySimpleGUI', 'plotly-express', 'kaleido', 'pandas', 'psutil']


userInput = input('++++++++++++++++++++++++++++++++++++++++++++++++++++\n'+
                'Möchtest du notwendige Abhängigkeiten installieren?\n'+
                '(das kann ein paar Minuten dauern...)\n'+
                'ENTER drücken zum überspringen\n'+
                'y und mit ENTER bestätigen zum installieren')
if userInput == 'y':
    try: 
        for i in dependencies:
            install(i)
    except Exception as e: 
        print('Das Programm konnte nicht geladen werden, wahrscheinlich fehlen Abhängigkeiten.\n' +
        'Diese sollten eigentlich über dieses Programm installiert werden, das hat nicht geklappt :-(\n'+
        'Folgende Bibliotheken müssen manuell installiert werden (mit Befehl zur Installation via PowerShell:\n\n'+
        'PySimpleGUI        <pip install PySimpleGUI>\n'+
        'Plotly Express     <pip install plotly-express>\n'+
        'Kaleido            <pip install kaleido>\n'+
        'Pandas             <pip install pandas>\n'+
        'PsUtil             <pip install psutil>\n\n'+
        'Wenn auch das nicht klappt bei der manuellen Installation --user als Flag hinter den Befehl setzen.\n'+
        'Und wenn auch das nicht klappt die Powershell oder cmd mal als Admin starten.')

        print('++++++++++++++++++++++++++++++++++++++++++++')
        print('Fehlermeldung:')
        print(e)

try:
    print('Starte Hauptprogramm...')
    from UserSelectionView import UserSelectionView
    UserSelectionView.initMainWindow()
except Exception as e:
    print(e)

