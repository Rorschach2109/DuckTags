from Src.DuckTagsDatabaseTools.DuckTagsMusicFileModel import DuckTagsMusicFileModel

from mutagen.easyid3 import EasyID3


class DuckTagsMp3MetadataManager(object):

    multiple_values_message = u'Multiple Values'

    def __init__(self):
        self.audio = None
        self.title_tag = u'title'
        self.artist_tag = u'artist'
        self.album_tag = u'album'
        self.genre_tag = u'genre'
        self.date_tag = u'date'
        self.track_number_tag = u'tracknumber'

    def __get_metadata_field__(self, metadata_field_name):
        try:
            return self.audio[metadata_field_name][0]
        except (KeyError, IndexError, TypeError):
            return u''

    def get_music_file_metadata(self, music_file_path):
        try:
            self.audio = EasyID3(music_file_path)
        except Exception:
            pass

        metadata_tags = dict()
        metadata_tags[self.title_tag] = self.__get_metadata_field__(self.title_tag)
        metadata_tags[self.artist_tag] = self.__get_metadata_field__(self.artist_tag)
        metadata_tags[self.album_tag] = self.__get_metadata_field__(self.album_tag)
        metadata_tags[self.genre_tag] = self.__get_metadata_field__(self.genre_tag)
        metadata_tags[self.date_tag] = self.__get_metadata_field__(self.date_tag)
        metadata_tags[self.track_number_tag] = self.__get_metadata_field__(self.track_number_tag)

        return DuckTagsMusicFileModel(music_file_path, metadata_tags)

    def get_music_files_list_metadata(self, music_files_paths_list):

        title_set = set()
        artist_set = set()
        album_set = set()
        genre_set = set()
        date_set = set()
        track_number_set = set()

        for music_file_path in music_files_paths_list:
            music_file_model = self.get_music_file_metadata(music_file_path)

            title_set.add(music_file_model.title)
            artist_set.add(music_file_model.artist)
            album_set.add(music_file_model.album)
            genre_set.add(music_file_model.genre)
            date_set.add(music_file_model.date)
            track_number_set.add(music_file_model.tracknumber)

        metadata_tags = dict()

        metadata_tags[self.title_tag] = title_set.pop() if len(title_set) == 1 \
            else self.multiple_values_message
        metadata_tags[self.album_tag] = album_set.pop() if len(album_set) == 1 \
            else self.multiple_values_message
        metadata_tags[self.genre_tag] = genre_set.pop() if len(genre_set) == 1 \
            else self.multiple_values_message
        metadata_tags[self.date_tag] = date_set.pop() if len(date_set) == 1 \
            else self.multiple_values_message
        metadata_tags[self.track_number_tag] = track_number_set.pop() if len(track_number_set) == 1 \
            else self.multiple_values_message

        return DuckTagsMusicFileModel(self.multiple_values_message, metadata_tags)

    def set_music_file_metadata(self, music_file_path, music_metadata_dict):
        try:
            self.audio = EasyID3(music_file_path)
        except Exception:
            pass
        else:
            self.audio[self.title_tag] = music_metadata_dict.get(self.title_tag,
                                                                 self.__get_metadata_field__(self.title_tag))
            self.audio[self.album_tag] = music_metadata_dict.get(self.album_tag,
                                                                 self.__get_metadata_field__(self.album_tag))
            self.audio[self.genre_tag] = music_metadata_dict.get(self.genre_tag,
                                                                 self.__get_metadata_field__(self.genre_tag))
            self.audio[self.date_tag] = music_metadata_dict.get(self.date_tag,
                                                                self.__get_metadata_field__(self.date_tag))
            self.audio[self.track_number_tag] = \
                music_metadata_dict.get(self.track_number_tag, self.__get_metadata_field__(self.track_number_tag))

            self.audio.save()

    def set_music_file_list_metadata(self, music_files_paths_list, music_metadata_dict):
        for music_file_path in music_files_paths_list:
            self.set_music_file_metadata(music_file_path, music_metadata_dict)