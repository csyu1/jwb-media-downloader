JWB Media Downloader uses the API of `tv.jw.org` to download and check for new files.

To install:

```
git clone https://github.com/csyu1/jwb-media-downloader.git
cd jwb-media-downloader/
pip install -r requirements.txt
```

So far, only the following primary categories are supported for download:
* Morning Worship
* Original Songs
* Introduction to Bible Books videos
* NWT Audio Recordings
* Original Songs Music Videos

To run the downloader, simply run
```
python main.py
```

By default, it will download all categories. To remove a category to download, simply comment out the line
in the `downloaders` variable in `main.py`.


### Defaults
```
The following is the default `config.py`.
PROXY_DICT = {
    "http": "",
    "https": "",
    "ftp": "",
}

LANGUAGE_JSON = 'https://data.jw-api.org/mediator/v1/languages/E/web?clientType=web'
LANGUAGE_KEY = 'E'
NWT_AUDIO_JSON = 'https://apps.jw.org/GETPUBMEDIALINKS?booknum=0&output=json&pub=nwt&fileformat=MP3%2CAAC&alllangs=0&langwritten=E&txtCMSLang=E'
JWB_API = 'https://data.jw-api.org/mediator/v1/categories/%s/' % (LANGUAGE_KEY,)

VIDEO_QUALITY = '240p'
DOWNLOAD_ROOT = 'files/%s/' % (LANGUAGE_KEY,)
WITH_SUBTITLES = False

DOWNLOAD_PATH = {
    'Morning Worship': DOWNLOAD_ROOT + 'morning_worship/',
    'Original Songs': DOWNLOAD_ROOT + 'original_songs/',
    'Bible Books': DOWNLOAD_ROOT + 'bible_books/',
    'New World Translation Audio': DOWNLOAD_ROOT + 'nwt_audio/',
    'Original Songs Music Video': DOWNLOAD_ROOT + 'original_songs_vod/',
}

CHECK_FIlE_INTEGRITY = True
```

To change any of these settings, simply edit `config.py` and run `main.py`.
