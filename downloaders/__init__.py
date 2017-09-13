from config import NWT_AUDIO_JSON

from core import JWBroadcastingDownloader
from core import JWBroadcastingVideoDownloader
from core import JWBroadcastingAudioDownloader

from core.mixins import TitleWithDateNoSpaceMixin, TitleBibleBookMixin


class VODOriginalSongsDownloader(JWBroadcastingVideoDownloader):

    key = 'Original Songs Music Video'


class OriginalSongsDownloader(JWBroadcastingAudioDownloader):

    key = 'Original Songs'


class MorningWorshipDownloader(TitleWithDateNoSpaceMixin, JWBroadcastingVideoDownloader):

    key = 'Morning Worship'


class BibleBooksDownloader(TitleBibleBookMixin, JWBroadcastingVideoDownloader):

    key = 'Bible Books'


class NWTAudioDownloader(JWBroadcastingDownloader):

    key = 'New World Translation Audio'

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
