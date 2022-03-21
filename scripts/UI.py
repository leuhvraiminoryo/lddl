import threading, PySimpleGUI as sg
import scripts.download as dl

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

def run():
    layout = [  [sg.Text('Bonjour et bienvenue à notre application de téléchargement de vidéos youtube',key='first')],
            [sg.Text('téléchargement actuel :'),sg.Text('Aucun',key ='filename')],
            [sg.Text('progression du téléchargement :'),sg.Text('Aucun',key ='progress')],
            [sg.Text('Votre URL :'), sg.InputText()],
            [sg.Text('Choisissez votre format de fichier :'), sg.OptionMenu(['mp4','mp3'],key='Format')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Downloader', layout,finalize=True)

    while True:

        event, values = window.read(1000)
        
        window['filename'].update(dl.status['dl_of_name'])
        window['progress'].update(dl.status['percentage'])
        window.refresh()

        if 'Format' == 'mp3':
            dl.ydl_opts['format'] = 'bestaudio'

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            dl.status['downloading'] = True
            load_thread = threading.Thread(target=dl.load,args=(values[0],))
            load_thread.start()
 

    window.close()