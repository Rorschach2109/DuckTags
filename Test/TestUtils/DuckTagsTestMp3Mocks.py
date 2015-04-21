class DuckTagsMP3AudioMock(object):
    def __init__(self):
        self.title = [u'title']
        self.album = [u'album']
        self.genre = [u'genre']
        self.date = [u'date']
        self.track_number = [u'track_number']

    def __getitem__(self, key):
        if key == u'title':
            return self.title
        elif key == u'album':
            return self.album
        elif key == u'genre':
            return self.genre
        elif key == u'date':
            return self.date
        elif key == u'tracknumber':
            return self.track_number

    def __setitem__(self, key, value):
        if key == u'title':
            self.title = [value]
        elif key == u'album':
            self.album = [value]
        elif key == u'genre':
            self.genre = [value]
        elif key == u'date':
            self.date = [value]
        elif key == u'tracknumber':
            self.track_number = [value]

    def get_tags_dict(self):
        return {
            u'title': self.title[0],
            u'album': self.album[0],
            u'genre': self.genre[0],
            u'date': self.date[0],
            u'tracknumber': self.track_number[0]
        }

    def save(self):
        pass