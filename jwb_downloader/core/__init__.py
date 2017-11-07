import os
import re
import json
import hashlib
import requests
from os.path import splitext
from urllib import request

from ..config import *


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class JWBroadcastingDownloader:

    def __init__(self, category=None, dated_title=False):
        self.download_info = []
        self.category = category
        self.dated_title = dated_title

    def download_json(self, json_url):
        r = requests.get(json_url, proxies=PROXY_DICT)
        media = json.loads(r.text)
        return media

    def get_title(self, media, file_meta):
        if not self.dated_title:
            return media['title']
        else:
            title = media['title']
            url = file_meta['progressiveDownloadURL']
            expression = r'20\d\d\d\d_\d\d'
            date = re.search(expression, url).group(0)
            title_with_date = '[%s]%s' % (date, title)
            return title_with_date

    def get_download_urls(self):
        json_url = JWB_API + self.category
        media_json = self.download_json(json_url)
        media_list = media_json['category']['media']
        for media in media_list:
            self.download_info.append(self.get_relevant_download_info(media))

    @property
    def download_path(self):
        return DOWNLOAD_ROOT + self.category + '/'

    def download_media(self):
        for (url, title, checksum) in self.download_info:
            _, extension = splitext(url)
            print(self.download_file(
                self.download_path,
                url, title, extension, checksum))

    def check_if_file_does_not_exist_or_corrupt(self, path, file, checksum):
        # TODO: Add checksum
        if file in os.listdir(path) and checksum == md5(path + file):
            return False
        return True

    def download_file(self, path, url, title, extension, checksum):
        status = title + ": {}"
        if not os.path.exists(path):
            os.makedirs(path)

        if not self.check_if_file_does_not_exist_or_corrupt(
                path, title + extension, checksum):
            return status.format("File present")

        try:
            request.urlretrieve(url, path + title + extension)
        except Exception:
            return status.format("Error")

        return status.format("Ok")

    def __call__(self):
        self.get_download_urls()
        self.download_media()

    def get_relevant_download_info(self, media):
        return self.get_url_title_checksum(media, 0)

    def get_url_title_checksum(self, media, file_index):
        f = media['files'][0]
        url = f['progressiveDownloadURL']
        title = self.get_title(media, f)
        checksum = f['checksum']
        return url, title, checksum


class JWBroadcastingVideoDownloader(JWBroadcastingDownloader):

    @property
    def download_path(self):
        return DOWNLOAD_ROOT + 'video/' + self.category + '/'

    def get_relevant_download_info(self, media):
        # default to first if no media found
        file_index = 0
        for index, f in enumerate(media['files']):
            if f['label'] == VIDEO_QUALITY and f['subtitled'] == WITH_SUBTITLES:
                file_index = index
                break
        return self.get_url_title_checksum(media, file_index)


class JWBroadcastingAudioDownloader(JWBroadcastingDownloader):

    @property
    def download_path(self):
        return DOWNLOAD_ROOT + 'audio/' + self.category + '/'