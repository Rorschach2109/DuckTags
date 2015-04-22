from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Utils.DuckTagsUtils import DuckTagsUtils

import os


class DuckTagsFolderStructureManager(object):
    def __init__(self):
        self.utils = DuckTagsUtils()
        self.metadata_api = DuckTagsMetadataAPI()

    def get_available_files_format_patterns(self):
        return [format_pattern_tuple[0] for format_pattern_tuple in self.utils.file_format_patterns]

    def reorganize_files_with_pattern(self, files_paths_list, file_format_pattern_index):
        for file_path in files_paths_list:
            self.__reorganize_file_with_pattern__(file_path, file_format_pattern_index)

    def __reorganize_file_with_pattern__(self, file_path, file_format_pattern_index):
        if not os.path.isfile(file_path):
            return

        self.__slice_file_path__(file_path)

        if not self.__convert_file_name_with_pattern__(file_path, file_format_pattern_index):
            return

        new_file_path = self.__join_file_path__()

        if not os.path.exists(new_file_path):
            os.rename(file_path, new_file_path)

    def __slice_file_path__(self, file_path):
        file_path_root_length = file_path.rfind(r'/') + 1
        self.file_path_root = file_path[:file_path_root_length]

        file_path_extension_start = file_path.rfind(r'.')
        self.file_extension = file_path[file_path_extension_start:]

        self.file_name = file_path[file_path_root_length:file_path_extension_start]

    def __join_file_path__(self):
        return ''.join([
            self.file_path_root,
            self.file_name,
            self.file_extension
        ])

    def __convert_file_name_with_pattern__(self, file_path, file_format_pattern_index):
        if file_format_pattern_index >= len(self.utils.file_format_patterns):
            return False

        metadata_tags_dict = self.metadata_api.get_music_file_metadata(file_path)
        if not metadata_tags_dict:
            return False

        track_number = metadata_tags_dict['tracknumber']
        title = metadata_tags_dict['title']

        if file_format_pattern_index == 0 or file_format_pattern_index == 1:
            self.file_name = self.utils.file_format_patterns[file_format_pattern_index][1] % (track_number, title)

        return True