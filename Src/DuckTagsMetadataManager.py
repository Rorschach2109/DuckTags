from Src.DuckTagsMp3MetadataManager import DuckTagsMp3MetadataManager

import functools


def __get_metadata_manager_index__(music_file_path):
    file_name = music_file_path.lower()

    if file_name.endswith('mp3'):
        manager_index = 0
    else:
        manager_index = None

    return manager_index


def music_file_type(metadata_handler_function):

    @functools.wraps(metadata_handler_function)
    def wrapper(instance, *args):
        music_file_path = args[0]
        DuckTagsMetadataManager.metadata_manager_index = __get_metadata_manager_index__(music_file_path)
        return metadata_handler_function(instance, *args)

    return wrapper


def music_files_list_type(metadata_handler_function):

    @functools.wraps(metadata_handler_function)
    def wrapper(instance, *args):
        music_file_type_set = set()
        music_files_paths_list = args[0]
        for music_file_path in music_files_paths_list:
            music_file_type_set.add(__get_metadata_manager_index__(music_file_path))

        if len(music_file_type_set) == 1:
            DuckTagsMetadataManager.metadata_manager_index = music_file_type_set.pop()
        else:
            DuckTagsMetadataManager.metadata_manager_index = None

        return metadata_handler_function(instance, *args)

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
        except TypeError:
            pass
        else:
            return metadata_manager.get_music_file_metadata(music_file_path)

    @music_files_list_type
    def get_music_files_list_metadata(self, music_files_paths_list):
        try:
            metadata_manager = self.metadata_managers_list[self.metadata_manager_index]
        except TypeError:
            pass
        else:
            return metadata_manager.get_music_files_list_metadata(music_files_paths_list)

    @music_file_type
    def set_music_file_metadata(self, music_file_path, music_metadata_dict):
        try:
            metadata_manager = self.metadata_managers_list[self.metadata_manager_index]
        except TypeError:
            pass
        else:
            return metadata_manager.set_music_file_metadata(music_file_path, music_metadata_dict)
