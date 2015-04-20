import os


class DuckTagsFileManager(object):

    current_folder_path = ''

    def __init__(self):
        self.music_extensions_list = []

    def get_files_dict_from_folder(self, folder_path):
        self.current_folder_path = folder_path

        files_dict = {}
        for (dir_path, dir_names, file_names) in os.walk(folder_path):
            files_dict[dir_path] = file_names
        return files_dict

    def get_music_files_from_files_dict(self, files_dict, music_extensions_list):
        self.music_extensions_list = list(set(music_extensions_list))

        filter_function = filter
        music_files_dict = {}
        for folder_name in files_dict:
            music_files_dict[folder_name] = filter_function(
                lambda file_name: file_name.endswith(tuple(self.music_extensions_list)),
                files_dict[folder_name]
            )

        return music_files_dict