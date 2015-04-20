from Src.DuckTagsMp3MetadataManager import DuckTagsMp3MetadataManager

import functools


def __get_metadata_manager_index__(music_file_path):
    file_name = music_file_path.lower()

    if file_name.endswith('mp3'):
        manager_index = 0
    else:
        manager_index = -1

    return manager_index


def music_file_type(get_metadata_function):

    @functools.wraps(get_metadata_function)
    def wrapper(instance, music_file_path):
        DuckTagsMetadataManager.metadata_manager_index = __get_metadata_manager_index__(music_file_path)
        return get_metadata_function(instance, music_file_path)

    return wrapper


def music_files_list_type(get_metadata_function):

    @functools.wraps(get_metadata_function)
    def wrapper(instance, music_files_paths_list):
        music_file_type_set = set()
        for music_file_path in music_files_paths_list:
            music_file_type_set.add(__get_metadata_manager_index__(music_file_path))

        if len(music_file_type_set) == 1:
            DuckTagsMetadataManager.metadata_manager_index = music_file_type_set.pop()
        else:
            DuckTagsMetadataManager.metadata_manager_index = -1

        return get_metadata_function(instance, music_files_paths_list)

    return wrapper


class DuckTagsMetadataManager(object):

    metadata_managers_list = [
        DuckTagsMp3MetadataManager()
    ]
    metadata_manager_index = None

    @music_file_type
    def get_music_file_metadata(self, music_file_path):
        try:
            metadata_manager = self.metadata_managers_list[self.metadata_manager_index]
        except IndexError:
            raise
        else:
            return metadata_manager.get_music_file_metadata(music_file_path)

    @music_files_list_type
    def get_music_files_list_metadata(self, music_files_paths_list):
        try:
            metadata_manager = self.metadata_managers_list[self.metadata_manager_index]
        except IndexError:
            raise
        else:
            return metadata_manager.get_music_files_list_metadata(music_files_paths_list)
