from Src.DuckTagsMp3MetadataManager import DuckTagsMp3MetadataManager

import functools


def __get_metadata_manager_index__(music_file_path):
    file_name = music_file_path.lower()

    if file_name.endswith('mp3'):
        manager_index = 0
    else:
        manager_index = -1

    return manager_index


def music_type_decorator(get_metadata_function):

    @functools.wraps(get_metadata_function)
    def wrapper(instance, music_file_path):
        DuckTagsMetadataManager.metadata_manager_index = __get_metadata_manager_index__(music_file_path)
        return get_metadata_function(instance, music_file_path)

    return wrapper


class DuckTagsMetadataManager(object):

    metadata_managers_list = [
        DuckTagsMp3MetadataManager()
    ]
    metadata_manager_index = -1

    @music_type_decorator
    def get_music_file_metadata(self, music_file_path):
        try:
            return self.metadata_managers_list[self.metadata_manager_index].get_music_file_metadata(music_file_path)
        except IndexError:
            raise

    def get_music_files_list_metadata(self, music_files_paths_list):
        pass