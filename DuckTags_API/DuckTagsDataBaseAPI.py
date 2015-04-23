from Src.DuckTagsDataBaseManager import DuckTagsDataBaseManager


class DuckTagsDataBaseAPI(object):
    def __init__(self):
        self.data_base_manager = DuckTagsDataBaseManager()

    def scan_folder(self, folder_path):
        return self.data_base_manager.scan_folder(folder_path)

    def search_for_file(self, search_option, search_pattern):
        return self.data_base_manager.search_for_file(search_option, search_pattern)