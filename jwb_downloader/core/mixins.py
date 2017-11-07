import re


class TitleBibleBookMixin(object):
    def get_title(self, media, file_meta):
        title = media['title']
        natural_key = media['naturalKey']
        expression = r'pub-nwtsv_E_(\d+)_VIDEO'
        ordering = re.search(expression, natural_key).group(1)
        title_with_ordering = "[%s] %s" % (ordering, title)
        return title_with_ordering
