from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI
from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Src.DuckTagsDatabaseTools import DuckTagsDataBaseIndexes
from Src.DuckTagsDatabaseTools import DuckTagsMusicFileModel

import functools

from CodernityDB.database import Database, RecordNotFound
from CodernityDB.index import IndexConflict


def database_access(foo):

    @functools.wraps(foo)
    def wrapper(manager, *args):
        try:
            manager.db.create()
            for index in manager.db_indexes:
                manager.db.add_index(index)
        except IndexConflict:
            manager.db.open()
            manager.db.reindex()

        return foo(manager, *args)

    return wrapper


class DuckTagsDataBaseManager(object):
    def __init__(self):
        self.file_api = DuckTagsFileAPI()
        self.metadata_api = DuckTagsMetadataAPI()
        self.db_name = u'DuckTagsDB'
        self.db = Database(self.db_name)
        self.db_indexes = [
            DuckTagsDataBaseIndexes.MusicPathIndex(self.db.path, 'path')
        ]

    def scan_folder(self, folder_path):
        music_files_dict = self.__get_music_files_from_folder__(folder_path)
        self.__insert_music_files_to_db__(music_files_dict)

    @database_access
    def clean_db(self):
        self.__clean_db__()
        self.__clean_indexes__()

    def search_for_file(self, search_option, search_pattern):
        pass

    def __get_music_files_from_folder__(self, folder_path):
        files_dict = self.file_api.get_files_dict_from_folder(folder_path)
        return self.file_api.get_music_files_from_files_dict(files_dict)

    @database_access
    def __insert_music_files_to_db__(self, music_files_dict):
        music_file_path_generator = self.__get_music_file_path__(music_files_dict)
        for music_file_path in music_file_path_generator:
            music_file_tags = self.metadata_api.get_music_file_metadata(music_file_path)
            music_file_model = DuckTagsMusicFileModel.DuckTagsMusicFileModel(music_file_path, music_file_tags)
            self.__insert_music_file_model__(music_file_model)

    def __insert_music_file_model__(self, music_file_model):
        try:
            self.db.get('path', music_file_model.path)
        except RecordNotFound:
            self.db.insert(music_file_model.serialize())

    @staticmethod
    def __get_music_file_path__(music_files_dict):
        directories = sorted(music_files_dict.keys())

        for directory in directories:
            for music_file in music_files_dict[directory]:
                yield '/'.join([directory.rstrip('/'), music_file])

    def __clean_db__(self):
        for db_element in self.db.all('id'):
            self.db.delete(db_element)

    def __clean_indexes__(self):
        for index in self.db_indexes:
            self.db.destroy_index(index)

        self.db_indexes = []