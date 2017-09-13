from downloaders import *
from constants import CATEGORIES

# TODO: be more user-friendly
if __name__ == '__main__':
    downloaders = [
        MorningWorshipDownloader,
        OriginalSongsDownloader,
        BibleBooksDownloader,
        NWTAudioDownloader,
        VODOriginalSongsDownloader,
    ]
    for index, downloader in enumerate(downloaders):
        print("Downloading " + CATEGORIES[index])
        dl = downloaders[index]()
        dl()
