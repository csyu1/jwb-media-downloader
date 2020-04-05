import json

import click
import requests

from ..config import JWB_API
from ..config import PROXY_DICT
from ..config import CHECK_FOR_NEW_CATEGORIES


def get_audio_categories(language):
    audio_url = JWB_API.format('E') + 'Audio/?detailed=1'
    audio_primary_categories = set()
    r = requests.get(audio_url, proxies=PROXY_DICT)
    audio_list = json.loads(r.text)['category']['subcategories']
    for audio in audio_list:
        audio_primary_categories.add(audio['media'][0]['primaryCategory'])
    # NWT Audio Recordings not served in tv.jw.org. Add manually.
    audio_primary_categories.add("NWTAudio")
    return audio_primary_categories


def get_video_categories(language):
    video_primary_categories = set()
    videos_url = JWB_API.format('E') + 'AllVideos/?detailed=1'
    r = requests.get(videos_url, proxies=PROXY_DICT)
    video_list = json.loads(r.text)['category']['media']
    for video in video_list:
        video_primary_categories.add(video['primaryCategory'])
    # Add manually since under tag "AllVideosExclude"
    video_primary_categories.add("VODSJJMeetings")
    return video_primary_categories


def get_categories(categories_filename=None):
    if categories_filename is None:
        categories_filename = 'categories.json'

    with open(categories_filename) as cat_file:
        dictionary = json.loads(cat_file.read())
        if not all(cat in dictionary.keys() for cat in ('audio', 'video')):
            raise Exception('Improper JSON Configuraiton')

    return dictionary


def update_categories(categories_filename=None, language=None):
    if categories_filename is None:
        categories_filename = 'categories.json'

    if language is None:
        language = 'E'

    audio_primary_categories = None
    video_primary_categories = None

    dictionary = {
        "video": {},
        "audio": {}
    }

    try:
        dictionary = get_categories(categories_filename)
    except Exception as e:
        click.echo("Error:", e)
        click.echo(f"Resetting {categories_filename} file.")

    audio_primary_categories = get_audio_categories(language)
    video_primary_categories = get_video_categories(language)
    dictionary['video'].update({v: 0 for v in video_primary_categories if v not in dictionary['video']})
    dictionary['audio'].update({a: 0 for a in audio_primary_categories if a not in dictionary['audio']})

    with open(categories_filename, 'w') as cat_file:
        json.dump(dictionary, cat_file, indent=2, sort_keys=True)
    return dictionary
