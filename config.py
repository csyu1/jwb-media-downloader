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
