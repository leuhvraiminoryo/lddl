from __future__ import unicode_literals
import youtube_dl, os

global status 

status = {
    'downloading': False,
    'dl_of_name': None,
    'percentage': None,
    'format' : '',
    'audio_only' : False
}

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def change_file(dic,ind,th):
    dic[ind]=th

def my_hook(d):

    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        status['downloading'] = False
        if status['audio_only']:
            os.rename(os.getcwd()+'\\'+d['filename'],d['filename'][:-16] + '.'+status['format'])
    else:
        change_file(status,'dl_of_name',d['filename'][:-16])
        change_file(status,'percentage',str(round(d['downloaded_bytes']/d['total_bytes']*100,2))+'%')


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

