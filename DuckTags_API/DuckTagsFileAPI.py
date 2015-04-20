from Src.DuckTagsFileManager import DuckTagsFileManager


class DuckTagsFileAPI(object):
    def __init__(self):
        self.file_manager = DuckTagsFileManager()

    def get_files_dict_from_folder(self, folder_path):
        return self.file_manager.get_files_dict_from_folder(folder_path)

    def get_music_files_from_files_dict(self, files_dict, music_extensions_list):
        return self.file_manager.get_music_files_from_files_dict(files_dict, music_extensions_list)

    def get_current_directory(self):
        return self.file_manager.get_current_directory()
