import re


class TitleBibleBookMixin(object):
    def get_title(self, media, file_meta):
        title = media['title']
        natural_key = media['naturalKey']
        expression = 'pub-nwtsv_%s_(\d+)_VIDEO' % (self.language)
        ordering = re.search(expression, natural_key).group(1)
        title_with_ordering = "[%s] %s" % (ordering, title)
        return title_with_ordering
