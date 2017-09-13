import os
import re


class TitleWithDateNoSpaceMixin(object):
    def get_title(self, media, file_meta):
        title = super(TitleWithDateNoSpaceMixin, self).get_title(media, file_meta)
        url = file_meta['progressiveDownloadURL']
        expression = r'20\d\d\d\d_\d\d'
        date = re.search(expression, url).group(0)
        title_with_date = '[%s]%s' % (date, title)
        return title_with_date


class TitleBibleBookMixin(object):
    def get_title(self, media, file_meta):
        title = super(TitleBibleBookMixin, self).get_title(media, file_meta)
        natural_key = media['naturalKey']
        expression = r'pub-nwtsv_E_(\d+)_VIDEO'
        ordering = re.search(expression, natural_key).group(1)
        title_with_ordering = "[%s] %s" % (ordering, title)
        return title_with_ordering


class TitleWithDateMixin(object):
    def get_title(self, media, file_meta):
        title = super(TitleWithDateMixin, self).get_title(media, file_meta)
        url = file_meta['progressiveDownloadURL']
        expression = r'20\d\d\d\d_\d\d'
        date = re.search(expression, url).group(0)
        title_with_date = '[%s] %s' % (date, title)
        return title_with_date


class OriginalFileTitleMixin(object):
    def get_title(self, media, file_meta):
        url = file_meta['progressiveDownloadURL']
        filename, extension = os.path.splitext(os.path.basename(url))
        return filename
