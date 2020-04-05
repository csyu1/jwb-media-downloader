from ..config import NWT_AUDIO_JSON
from ..config import DOWNLOAD_ROOT

from ..core import JWBroadcastingDownloader
from ..core import JWBroadcastingVideoDownloader

from ..core.mixins import TitleBibleBookMixin


class BibleBooksDownloader(TitleBibleBookMixin, JWBroadcastingVideoDownloader):

    def __init__(self, language_key=None):
        category = 'BibleBooks'
        if not language_key:
            self.language = 'E'
        self.language = language_key
        super(BibleBooksDownloader, self).__init__(category, language_key=language_key)


class NWTAudioDownloader(JWBroadcastingDownloader):

    @property
    def download_path(self):
        return self.download_root + 'NWTAudio/'

    def get_download_urls(self):
        json_url = NWT_AUDIO_JSON
        media_json = self.download_json(json_url)
        media_list = media_json['files']['E']['MP3']
        for media in media_list:
            self.download_info.append(self.get_relevant_download_info(media))

    def get_relevant_download_info(self, media):
        url = media['file']['url']
        title = self.get_title(media)
        checksum = media['file']['checksum']
        return url, title, checksum

    def get_title(self, media):
        title = media['title']
        booknum = str(media['booknum']).zfill(2)
        title_with_ordering = '[%s] %s' % (booknum, title)
        return title_with_ordering
