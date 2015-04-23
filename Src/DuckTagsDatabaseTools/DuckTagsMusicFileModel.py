class DuckTagsMusicFileModel(object):
    def __init__(self, music_file_path, metadata_tags_dict):
        self.path = music_file_path

        self.title = metadata_tags_dict.get(u'title', u'')
        self.artist = metadata_tags_dict.get(u'artist', u'')
        self.album = metadata_tags_dict.get(u'album', u'')
        self.genre = metadata_tags_dict.get(u'genre', u'')
        self.date = metadata_tags_dict.get(u'date', u'')
        self.tracknumber = metadata_tags_dict.get(u'tracknumber', u'')

    def serialize(self):
        return self.__dict__