from __future__ import unicode_literals
import threading
import youtube_dl

ydl_opts = {}
def load(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

