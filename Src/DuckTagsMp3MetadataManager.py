from Src.DuckTagsDatabaseTools.DuckTagsMusicFileModel import DuckTagsMusicFileModel
from Utils.DuckTagsExceptions import DuckTagsMultipleCoverDirectories

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

import os


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
        self.cover_tag = u'APIC:'

        self.cover_file_name = u'Cover'
        self.png_file_extension = u'png'
        self.jpg_file_extension = u'jpg'

        self.apic_encoding_utf = 3
        self.apic_mime_tag = u'image'
        self.apic_cover_type = 3

    def __get_metadata_field__(self, metadata_field_name):
        try:
            return self.audio[metadata_field_name][0]
        except (KeyError, IndexError, TypeError):
            return u''

    def __get_metadata_fields_to_set__(self, music_metadata_dict, tag_name):
        try:
            tag_value = music_metadata_dict[tag_name]
            if tag_value == self.multiple_values_message:
                raise ValueError
        except (KeyError, ValueError):
            tag_value = self.__get_metadata_field__(tag_name)
        finally:
            self.audio[tag_name] = tag_value

    @staticmethod
    def __do_uppercase_tag_value__(tag_value):
        return ''.join([x[:1].upper() + x[1:].lower() + ' ' for x in tag_value.split(' ')]).rstrip()

    def get_music_file_metadata(self, music_file_path):
        metadata_tags = dict()

        try:
            self.audio = EasyID3(music_file_path)
        except Exception:
            pass
        else:
            metadata_tags[self.title_tag] = self.__get_metadata_field__(self.title_tag)
            metadata_tags[self.artist_tag] = self.__get_metadata_field__(self.artist_tag)
            metadata_tags[self.album_tag] = self.__get_metadata_field__(self.album_tag)
            metadata_tags[self.genre_tag] = self.__get_metadata_field__(self.genre_tag)
            metadata_tags[self.date_tag] = self.__get_metadata_field__(self.date_tag)
            metadata_tags[self.track_number_tag] = self.__get_metadata_field__(self.track_number_tag)
        finally:
            self.audio = None

        return DuckTagsMusicFileModel(music_file_path, metadata_tags)

    def get_music_files_list_metadata(self, music_files_paths_list):

        if len(music_files_paths_list) == 1:
            return self.get_music_file_metadata(music_files_paths_list[0])

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
        metadata_tags[self.artist_tag] = artist_set.pop() if len(artist_set) == 1 \
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

    def set_music_file_metadata(self, music_file_path, music_metadata_dict, cover_path):
        try:
            self.audio = EasyID3(music_file_path)
        except Exception:
            pass
        else:
            for tag_name in [self.title_tag, self.artist_tag, self.album_tag,
                             self.date_tag, self.track_number_tag, self.genre_tag]:
                self.__get_metadata_fields_to_set__(music_metadata_dict, tag_name)

            self.audio.save()

        finally:
            self.audio = None

    def set_music_file_list_metadata(self, music_files_paths_list, music_metadata_dict, cover_path):
        for music_file_path in music_files_paths_list:
            self.set_music_file_metadata(music_file_path, music_metadata_dict, cover_path)

        if cover_path:
            self.__set_music_file_list_cover__(music_files_paths_list, cover_path)

    def set_music_file_metadata_uppercase(self, music_file_path):
        try:
            self.audio = EasyID3(music_file_path)
        except Exception:
            pass
        else:
            for tag_name in [self.title_tag, self.artist_tag, self.album_tag, self.genre_tag]:
                tag_value = self.__get_metadata_field__(tag_name)
                uppercase_tag_value = self.__do_uppercase_tag_value__(tag_value)
                self.audio[tag_name] = uppercase_tag_value

            self.audio.save()
        finally:
            self.audio = None

    def set_music_file_list_metadata_uppercase(self, music_files_paths_list):
        for music_file_path in music_files_paths_list:
            self.set_music_file_metadata_uppercase(music_file_path)

    def get_music_files_list_cover(self, music_files_paths_list):
        try:
            cover_directory = self.__load_cover_from_directory__(music_files_paths_list)
        except DuckTagsMultipleCoverDirectories:
            return str()
        except IndexError:
            return self.__load_cover_from_tags__(music_files_paths_list)
        else:
            return cover_directory

    def __load_cover_from_directory__(self, music_files_paths_list):
        music_files_directories = set([file_path[:file_path.rfind('/')] for file_path in music_files_paths_list])

        if len(music_files_directories) == 1:
            directory_path = music_files_directories.pop()
            directory_images_list = self.__get_directory_images_list__(directory_path)

            return '/'.join([directory_path, directory_images_list[0]])
        else:
            raise DuckTagsMultipleCoverDirectories

    def __get_directory_images_list__(self, directory_path):
        return filter(
            lambda file_path:
            file_path.endswith(self.jpg_file_extension) or file_path.endswith(self.png_file_extension),
            os.listdir(directory_path)
        )

    def __load_cover_from_tags__(self, music_files_paths_list):
        cover_file_path = str()

        directory_path = self.__get_directory_path_from_music_file_path__(music_files_paths_list[0])
        for music_file_path in music_files_paths_list:
            try:
                self.audio = MP3(music_file_path, ID3=ID3)
            except Exception:
                continue
            else:
                if self.cover_tag in self.audio:
                    if self.png_file_extension.upper() in self.audio[self.cover_tag].data[:10].decode('ISO-8859-1'):
                        cover_extension = self.png_file_extension
                    else:
                        cover_extension = self.jpg_file_extension

                    cover_file_name = '.'.join([self.cover_file_name, cover_extension])
                    cover_file_path = '/'.join([directory_path, cover_file_name])

                    cover_file = open(cover_file_path, 'wb')
                    cover_file.write(self.audio[self.cover_tag].data)
                    cover_file.close()

                    break
            finally:
                self.audio = None

        return cover_file_path

    def __set_music_file_cover_in_directory__(self, destination_directory_path, cover_path):
        for music_file_name in filter(
                lambda file_name: file_name.endswith('.mp3'), os.listdir(destination_directory_path)
        ):
            music_file_path = '/'.join([destination_directory_path, music_file_name])
            try:
                self.audio = MP3(music_file_path, ID3=ID3)

            except Exception:
                continue

            else:
                cover_extension = self.__get_cover_extension_from_path__(cover_path)
                apic_mime = '/'.join([self.apic_mime_tag, cover_extension])
                self.audio.tags.add(
                    APIC(
                        encoding=self.apic_encoding_utf,
                        mime=apic_mime,
                        type=self.apic_cover_type,
                        desc=u'',
                        data=open(cover_path).read()
                    )
                )
                self.audio.save()

    def __set_music_file_list_cover__(self, music_files_paths_list, cover_path):
        destination_directory_path_list = self.__get_directory_path_from_music_files_path_list__(music_files_paths_list)

        for destination_directory_path in destination_directory_path_list:

            self.__set_music_file_cover_in_directory__(destination_directory_path, cover_path)
            self.__create_cover_file_in_directory__(destination_directory_path, cover_path)

            self.audio = None

    def __create_cover_file_in_directory__(self, destination_directory_path, cover_path):
        cover_file_name = '.'.join([self.cover_file_name, self.__get_cover_extension_from_path__(cover_path)])
        destination_cover_path = '/'.join([destination_directory_path, cover_file_name])

        self.__remove_old_image_files__(destination_directory_path)

        cover_file = open(destination_cover_path, 'wb')
        cover_file.write(self.audio[self.cover_tag].data)
        cover_file.close()

    def __get_cover_extension_from_path__(self, cover_path):
        if cover_path.endswith(self.png_file_extension):
            cover_extension = self.png_file_extension
        else:
            cover_extension = self.jpg_file_extension

        return cover_extension

    @staticmethod
    def __get_directory_path_from_music_file_path__(music_file_path):
        return music_file_path[:music_file_path.rfind('/')]

    def __get_directory_path_from_music_files_path_list__(self, music_files_paths_list):
        music_directories_list = list(
            set(
                map(self.__get_directory_path_from_music_file_path__, music_files_paths_list)
            )
        )
        return music_directories_list

    def __remove_old_image_files__(self, destination_directory_path):
        images_files_list = filter(
            lambda file_name:
            file_name.endswith(self.png_file_extension) or file_name.endswith(self.jpg_file_extension),
            os.listdir(destination_directory_path)
        )

        for image_file_path in map(
                lambda file_name: '/'.join([destination_directory_path, file_name]), images_files_list
        ):
            os.remove(image_file_path)