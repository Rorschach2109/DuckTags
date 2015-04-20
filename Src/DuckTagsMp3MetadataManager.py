from mutagen.easyid3 import EasyID3


class DuckTagsMp3MetadataManager(object):

    def __init__(self):
        self.audio = None

    def get_music_file_metadata(self, music_file_name):
        try:
            self.audio = EasyID3(music_file_name)
        except Exception:
            return dict()

        metadata_tags = dict()
        metadata_tags[u'title'] = self.__get_metadata_field__('title')
        metadata_tags[u'album'] = self.__get_metadata_field__('album')
        metadata_tags[u'genre'] = self.__get_metadata_field__('genre')
        metadata_tags[u'date'] = self.__get_metadata_field__('date')

        return metadata_tags

    def __get_metadata_field__(self, metadata_field_name):
        try:
            return self.audio[metadata_field_name][0]
        except KeyError:
            return u''