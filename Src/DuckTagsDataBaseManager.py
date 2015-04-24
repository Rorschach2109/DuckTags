from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI
from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Src.DuckTagsDatabaseTools import DuckTagsMusicFileModel

import functools

import sqlite3 as lite


def database_access(foo):

    @functools.wraps(foo)
    def wrapper(manager, *args):
        manager.connection = lite.connect(manager.db_name + '.db')

        manager.connection.close()
        manager.connection = None

    return wrapper


class DuckTagsDataBaseManager(object):
    def __init__(self):
        self.file_api = DuckTagsFileAPI()
        self.metadata_api = DuckTagsMetadataAPI()
        self.db_name = 'DuckTagsDB'

    def add_music_files_from_folder(self, folder_path):
        music_files_dict = self.__get_music_files_from_folder__(folder_path)
        self.__insert_music_files_to_db__(music_files_dict)

    def __get_music_files_from_folder__(self, folder_path):
        files_dict = self.file_api.get_files_dict_from_folder(folder_path)
        return self.file_api.get_music_files_from_files_dict(files_dict)

    @database_access
    def __insert_music_files_to_db__(self, music_files_dict):
        pass

    @database_access
    def clean_db(self):
        pass

    def search_for_files(self, search_option, search_pattern):
        pass