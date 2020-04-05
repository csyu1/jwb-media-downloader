import click

from jwb_downloader.config import DATED_CATEGORIES
from jwb_downloader.core.category_crawler import get_categories, update_categories
from jwb_downloader.core import JWBroadcastingVideoDownloader
from jwb_downloader.core import JWBroadcastingAudioDownloader
from jwb_downloader.downloaders import BibleBooksDownloader
from jwb_downloader.downloaders import NWTAudioDownloader

@click.group(
    help="Download Audio and Video files from jw.org"
)
def main():
    pass

@main.command(
    help="Download files in indicated categories JSON"
)
@click.option('--file', '-f', help="Select appropriate categories")
@click.option('--language', '-l', help="Select language")
def download(file=None, language=None):
    if not language:
        language = 'E'

    categories = get_categories(file)
    for key, value in categories['video'].items():
        if value == 1:
            click.echo(">> Downloading %s [%s] category" % (key, language))
            if key == 'BibleBooks':
                # different title format based on Bible ordering
                downloader = BibleBooksDownloader(language_key=language)
            else:
                downloader = JWBroadcastingVideoDownloader(
                    key, dated_title=key in DATED_CATEGORIES, language_key=language)
            downloader()

    for key, value in categories['audio'].items():
        if value == 1:
            click.echo(">> Downloading %s category" % key)
            if key == 'NWTAudio':
                # different download methods since downloaded from jw.org instead of tv.jw.org API
                downloader = NWTAudioDownloader()
            else:
                downloader = JWBroadcastingAudioDownloader(key, language_key=language)
            downloader()

@main.command(
    help="Update indicated categories JSON"
)
@click.option('--file', '-f', help="Update the Categories File")
def update(file=None):
    update_categories(file)
    click.echo("Updated")

if __name__ == '__main__':
    main()