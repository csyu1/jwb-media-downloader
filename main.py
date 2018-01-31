from jwb_downloader.config import DATED_CATEGORIES
from jwb_downloader.core.category_crawler import update_categories
from jwb_downloader.core import JWBroadcastingVideoDownloader
from jwb_downloader.core import JWBroadcastingAudioDownloader
from jwb_downloader.downloaders import BibleBooksDownloader
from jwb_downloader.downloaders import NWTAudioDownloader

if __name__ == '__main__':
    categories = update_categories()
    for key, value in categories['video'].items():
        if value == 1:
            print("~%s~" % key)
            if key == 'BibleBooks':
                # different title format based on Bible ordering
                downloader = BibleBooksDownloader()
            else:
                downloader = JWBroadcastingVideoDownloader(key, dated_title=key in DATED_CATEGORIES)
            downloader()

    for key, value in categories['audio'].items():
        if value == 1:
            print("~%s~" % key)
            if key == 'NWTAudio':
                # different download methods since downloaded from jw.org instead of tv.jw.org API
                downloader = NWTAudioDownloader()
            else:
                downloader = JWBroadcastingAudioDownloader(key)
            downloader()
