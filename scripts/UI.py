import threading, PySimpleGUI as sg
import scripts.download as dl
import sys, time

sg.theme('DarkAmber')   

audio_types = ['mp3']

def run():
    layout = [  [sg.Text('Bonjour et bienvenue à notre application de téléchargement de vidéos youtube',key='first')],
            [sg.Text('Votre URL :'), sg.InputText()],
            [sg.Text('Choisissez votre format de fichier :'), sg.OptionMenu(['mp4','mp3'],key='Format')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
    layout2 = [[ sg.Text('voir :'), sg.OptionMenu(['rien'],key='selected')], 
            [sg.Text('>> téléchargement actuel :'),sg.Text('Aucun',key ='filename')],
            [sg.Text('>> pourcentage :'),sg.Text('Aucun',key ='progress')],#,sg.Text('kilobytes :'),sg.Text('Aucun',key='kilobytes')]
            [sg.Text('>> vitesse de dl :'),sg.Text('Aucun',key='speed')],
            [sg.Text('>> temps restant :'),sg.Text('Aucun',key='eta')]]

    tabgrp = [[sg.TabGroup([[sg.Tab('Sélection téléchargements', layout, border_width =10),
                    sg.Tab('infos', layout2)]], tab_location='centertop', border_width=5)]]
    
    window = sg.Window('Downloader', tabgrp)


    while True:

        values = {'Format' : 'mp4'}
        event, values = window.read(1000)

        if values['selected'] not in ('',None,'rien','exemple'):
            selected = values['selected'].replace("'",'').replace('(','').replace(')','').replace(',','').split(' ')[0]
            print(selected)
        
            window['filename'].update(dl.status[selected]['dl_of_name'])
            window['progress'].update(dl.status[selected]['percentage'])
            #window['kilobytes'].update(dl.status[selected]['kilobytes'])
            window['speed'].update(dl.status[selected]['speed'])
            window['eta'].update(dl.status[selected]['eta'])

        window['selected'].update([i for i in dl.status.keys()])

        window.refresh()

        dl.status['format'] = values['Format']

        if values['Format'] in audio_types:
            dl.audio_only = True
            dl.ydl_opts['format'] = 'bestaudio/best'
        else:
            dl.audio_only = False
            dl.ydl_opts['format'] = 'best'
        
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            sys.exit('window closed')

        if event == 'Ok':
            load_thread = threading.Thread(target=dl.load,args=(values[0],))
            load_thread.start()