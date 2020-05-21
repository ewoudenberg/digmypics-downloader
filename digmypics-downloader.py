import json
import os
import sys
import time
import datetime

import requests

# Eric Woudenberg Spring 2020 (eaw@woudy.org)
# Free for all to use and modify

def usage():
    print(f'''
usage: {sys.argv[0]} <ORDER-NUMBER> <ZIP-CODE> <LOCAL-DOWNLOAD-DIRECTORY>

       The program downloads all files for the given order number into the given download directory.
       If the photo exists already in the download directory, it does not try to download it.
''')
    sys.exit(1)

class _opts:
    def __init__(self):
        argv = sys.argv[1:]
        if len(argv) != 3:
            usage()
        self.order_no = argv[0]
        self.zipcode = argv[1]
        self.dir = argv[2]
        self.url = f'https://www.digmypics.com/api/api/photos/get?oID={self.order_no}&sZip={self.zipcode}'

def get_filename(photo):
    return f'{get_dir(photo)}/{photo["Name"].replace("tif", "jpg")}'

def get_dir(photo):
    return f'{Opts.dir}/{photo["Folder"]}'

def get_photo_url(photo):
    return f'{photo["urlBase"]}/full/{Opts.order_no}/{photo["id"]}.jpg'

def exists(photo):
    filename = get_filename(photo)
    return os.path.exists(filename)

def download(photo):
    response = requests.get(get_photo_url(photo))
    if response.status_code != 200:
        print(f' -- could not access {photo}, got HTTP code {response.status_code}')
        return

    dir = get_dir(photo)
    if not os.path.exists(dir):
        os.makedirs(dir)

    filename = get_filename(photo)
    with open(filename, 'wb') as f:
        f.write(response.content)
    
class Download_progress:
    def __init__(self, photoset):
        self.photoset_len = len(photoset)
        self.to_download = len([photo for photo in photoset if not exists(photo)])
        self.download_start = time.time()
        self.downloaded_sofar = 0

    def did_download(self, i):
        self.downloaded_sofar += 1
        percent = i / self.photoset_len * 100
        self.percent = f'{percent:5.2f}%'
        self.eta = f'{self.get_eta():%Y-%m-%d %H:%M}'

    def get_eta(self):
        duration = time.time() - self.download_start
        sec_per_download = duration/self.downloaded_sofar
        remaining_seconds = sec_per_download * (self.to_download-self.downloaded_sofar)
        return datetime.datetime.now() + datetime.timedelta(seconds=remaining_seconds)

def process():
    response = requests.get(Opts.url)
    if response.status_code != 200:
        print(f'Could not access your photos, got HTTP code {response.status_code}')
        return
        
    photoset = json.loads(response.content)
    progress = Download_progress(photoset)
    print(f'{progress.photoset_len} photos in the order, {progress.to_download} left to go.')

    for i, photo in enumerate(photoset):
        if not exists(photo):
            print('downloading', get_filename(photo), end='', flush=True)

            start = time.time()
            download(photo)
            elapsed = time.time()-start

            progress.did_download(i)
            print(f' -- {elapsed:5.2f}s {progress.percent}  eta: {progress.eta}')

def main():
    global Opts
    Opts = _opts()
    process()

if __name__ == '__main__':
    main()
