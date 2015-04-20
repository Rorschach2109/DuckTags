from mutagen.easyid3 import EasyID3


class DuckTagsMp3MetadataManager(object):

    multiple_values_message = u'Multiple Values'

    def __init__(self):
        self.audio = None

    def __get_metadata_field__(self, metadata_field_name):
        try:
            return self.audio[metadata_field_name][0]
        except (KeyError, IndexError):
            return u''

    def get_music_file_metadata(self, music_file_path):
        try:
            self.audio = EasyID3(music_file_path)
        except Exception:
            return dict()

        metadata_tags = dict()
        metadata_tags[u'title'] = self.__get_metadata_field__('title')
        metadata_tags[u'album'] = self.__get_metadata_field__('album')
        metadata_tags[u'genre'] = self.__get_metadata_field__('genre')
        metadata_tags[u'date'] = self.__get_metadata_field__('date')

        return metadata_tags

    def get_music_files_list_metadata(self, music_files_paths_list):

        title_set = set()
        album_set = set()
        genre_set = set()
        date_set = set()

        for music_file_path in music_files_paths_list:
            try:
                self.audio = EasyID3(music_file_path)
            except Exception:
                continue

            title_set.add(self.__get_metadata_field__('title'))
            album_set.add(self.__get_metadata_field__('album'))
            genre_set.add(self.__get_metadata_field__('genre'))
            date_set.add(self.__get_metadata_field__('date'))

        metadata_tags = dict()
        metadata_tags[u'title'] = title_set.pop() if len(title_set) == 1 else self.multiple_values_message
        metadata_tags[u'album'] = album_set.pop() if len(album_set) == 1 else self.multiple_values_message
        metadata_tags[u'genre'] = genre_set.pop() if len(genre_set) == 1 else self.multiple_values_message
        metadata_tags[u'date'] = date_set.pop() if len(date_set) == 1 else self.multiple_values_message

        return metadata_tags