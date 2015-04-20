from mutagen.easyid3 import EasyID3


class DuckTagsMp3MetadataManager(object):

    def __init__(self):
        self.audio = None

    def get_music_file_metadata(self, music_file_name):
        try:
            self.audio = EasyID3(music_file_name)
        except Exception:
            return {}

        metadata_tags = dict()
        metadata_tags[u'title'] = self.__get_metadata_title__()
        metadata_tags[u'album'] = self.__get_metadata_album__()
        metadata_tags[u'genre'] = self.__get_metadata_genre__()
        metadata_tags[u'date'] = self.__get_metadata_date__()

        return metadata_tags

    def __get_metadata_title__(self):
        try:
            return self.audio['title'][0]
        except KeyError:
            return u''

    def __get_metadata_album__(self):
        try:
            return self.audio['album'][0]
        except KeyError:
            return u''

    def __get_metadata_genre__(self):
        try:
            return self.audio['genre'][0]
        except KeyError:
            return u''

    def __get_metadata_date__(self):
        try:
            return self.audio['date'][0]
        except KeyError:
            return u''