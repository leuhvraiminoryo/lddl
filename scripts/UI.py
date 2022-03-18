import threading, PySimpleGUI as sg
import scripts.download as dl

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Bonjour et bienvenue à notre application de téléchargement de vidéos youtube')],
            [sg.Text('Votre URL :'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
def run():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            load_thread = threading.Thread(target=dl.load,args=(values[0],))
            load_thread.start()

    window.close()