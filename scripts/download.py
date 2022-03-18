from __future__ import unicode_literals
import youtube_dl

status = {
    'downloading': False,
    'dl_of_name': None,
    'percentage': None
}

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if '_percent_str' in d.keys():
        status['dl_of_name'] = d['filename'][:-17]
        status['percentage'] = d['_percent_str']
    
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        status['downloading'] = False


ydl_opts = {
    'format': 'best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def load(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

