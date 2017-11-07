JWB Media Downloader uses the API of `tv.jw.org` to download and check for new files.

To install:

```
git clone https://github.com/csyu1/jwb-media-downloader.git
cd jwb-media-downloader/
pip install -r requirements.txt
```

To run the downloader, simply run
```
python main.py
```

The program will download all categories in the `categories.json` file with value set to 1.
To remove a category to download, simply change the value to 0 in the said file.


### Defaults
The following is the default `config.py`:
```
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

DATED_CATEGORIES = []
CHECK_FIlE_INTEGRITY = True
CHECK_FOR_NEW_CATEGORIES = True
```

`DATED_CATEGORIES` are a list of categories. The files under these categories will be downloaded with a datestamp prepended to the file title.

To change any of these settings, simply edit `config.py` and run `main.py`.


## IS THIS LEGAL?
Yes! Under jw.org's [terms of use](https://www.jw.org/en/terms-of-use/#link2):
> You may not:
> * Create for distribution purposes, any software applications, tools, or techniques
> that are specifically made to collect, copy, download, extract, harvest, or scrape
> data, HTML, images, or text from this site. (This does not prohibit the distribution
> of free, non-commercial applications designed to download electronic files such as
> EPUB, PDF, MP3, and MP4 files from public areas of this site.)
