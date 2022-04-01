from __future__ import unicode_literals
import youtube_dl, os

global status, audio_only

audio_only = [False]

status = {
    'exemple':
    {
        'dl_of_name': None,
        'percentage': None,
        'format' : '',
        'audio_only' : False,
        'kilobytes' : None,
        'speed' : None,
        'eta' : None
    }
}

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if not d['filename'][:10] in status.keys():
        status[d['filename'][:10]] = {}

    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        status[d['filename'][:10]]['downloading'] = False
        if status[d['filename'][:10]]['audio_only']:
            os.rename(os.getcwd()+'\\'+d['filename'],d['filename'][:-16] + '.'+status[d['filename'][:10]]['format'])
    else:
        status[d['filename'][:10]]['dl_of_name'] = d['filename'][:-16]
        status[d['filename'][:10]]['percentage'] = d['_percent_str']
        status[d['filename'][:10]]['speed'] = d['_speed_str']
        status[d['filename'][:10]]['eta'] = d['_eta_str']

        #status['kilobytes'] = str(d['downloaded_bytes']%1000)+' / '+str(d['total_bytes']%1000))


ydl_opts = {
    'format': 'best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp4',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def load(url):
    if url.startswith('https://'):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

