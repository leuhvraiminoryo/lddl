import threading, PySimpleGUI as sg
import scripts.download as dl
import os

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
audio_types = ['mp3']
def run():
    layout = [  [sg.Text('Bonjour et bienvenue à notre application de téléchargement de vidéos youtube',key='first')],
            [sg.Text('Votre URL :'), sg.InputText()],
            [sg.Text('Choisissez votre format de fichier :'), sg.OptionMenu(['mp4','mp3'],key='Format')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
    layout2 = [ [sg.Text('>> téléchargement actuel :'),sg.Text('Aucun',key ='filename')],
            [sg.Text('>> pourcentage :'),sg.Text('Aucun',key ='progress')],#,sg.Text('kilobytes :'),sg.Text('Aucun',key='kilobytes')]
            [sg.Text('>> vitesse de dl :'),sg.Text('Aucun',key='speed')],
            [sg.Text('>> temps restant :'),sg.Text('Aucun',key='eta')]]

    tabgrp = [[sg.TabGroup([[sg.Tab('Sélection téléchargements', layout, border_width =10),
                    sg.Tab('infos', layout2)]], tab_location='centertop', border_width=5)]]
    
    window = sg.Window('Downloader', tabgrp)

    while True:
        values = {'Format' : 'mp4'}
        event, values = window.read(1000)
        
        window['filename'].update(dl.status['dl_of_name'])
        window['progress'].update(dl.status['percentage'])
        #window['kilobytes'].update(dl.status['kilobytes'])
        window['speed'].update(dl.status['speed'])
        window['eta'].update(dl.status['eta'])

        window.refresh()

        if values['Format'] is not None:
            dl.status['format'] = values['Format']

        if values['Format'] in audio_types:
            dl.status['audio_only'] = True
            dl.ydl_opts['format'] = 'bestaudio/best'
        else:
            dl.status['audio_only'] = False
            dl.ydl_opts['format'] = 'best'
        
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if event == 'Ok':
            dl.status['downloading'] = True
            load_thread = threading.Thread(target=dl.load,args=(values[0],))
            load_thread.start()
 

    window.close()