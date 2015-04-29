from Src.DuckTagsFileManager import DuckTagsFileManager

import functools


def music_files_decorator(get_files_foo):

    @functools.wraps(get_files_foo)
    def wrapper(file_api, folder_path):
        files_dict = get_files_foo(file_api, folder_path)
        return file_api.get_music_files_from_files_dict(files_dict)

    return wrapper


class DuckTagsFileAPI(object):
    def __init__(self):
        self.file_manager = DuckTagsFileManager()
        self.music_extensions_list = [
            'mp3'
        ]

    @music_files_decorator
    def get_files_dict_from_folder(self, folder_path):
        return self.file_manager.get_files_dict_from_folder(folder_path)

    def get_music_files_from_files_dict(self, files_dict):
        return self.file_manager.get_music_files_from_files_dict(files_dict, self.music_extensions_list)

    def get_current_directory(self):
        return self.file_manager.get_current_directory()

    def set_music_extensions_list(self, music_extension_list):
        self.music_extensions_list = list(set(music_extension_list))