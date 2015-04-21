class DuckTagsMP3AudioMock(object):
    def __init__(self):
        self.title = [u'title']
        self.album = [u'album']
        self.genre = [u'genre']
        self.date = [u'date']

    def __getitem__(self, key):
        if key == u'title':
            return self.title
        elif key == u'album':
            return self.album
        elif key == u'genre':
            return self.genre
        elif key == u'date':
            return self.date

    def __setitem__(self, key, value):
        if key == u'title':
            self.title = [value]
        elif key == u'album':
            self.album = [value]
        elif key == u'genre':
            self.genre = [value]
        elif key == u'date':
            self.date = [value]

    def get_tags_dict(self):
        return {
            u'title': self.title[0],
            u'album': self.album[0],
            u'genre': self.genre[0],
            u'date': self.date[0]
        }

    def save(self):
        pass