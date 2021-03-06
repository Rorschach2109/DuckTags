from Src.DuckTagsDataBaseManager import DuckTagsDataBaseManager


class DuckTagsDataBaseAPI(object):
    def __init__(self):
        self.data_base_manager = DuckTagsDataBaseManager()
        self.data_base_manager.initialize_db()

    def add_music_files_from_folder(self, folder_path):
        return self.data_base_manager.add_music_files_from_folder(folder_path)

    def clean_db(self):
        return self.data_base_manager.clean_db()

    def search_for_files(self, search_option, search_pattern):
        return self.data_base_manager.search_for_files(search_option, search_pattern)