from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Utils.DuckTagsUtils import DuckTagsUtils

import os


class DuckTagsFolderStructureManager(object):
    def __init__(self):
        self.utils = DuckTagsUtils()
        self.metadata_api = DuckTagsMetadataAPI()

    def get_available_files_format_patterns(self):
        return self.utils.file_format_patterns

    def get_available_folders_format_patterns(self):
        pass

    def get_preview(self):
        pass

    def reorganize_files_with_pattern(self, files_paths_list, file_format_pattern_index):
        for file_path in files_paths_list:
            self.__reorganize_file_with_pattern__(file_path, file_format_pattern_index)

    def __reorganize_file_with_pattern__(self, file_path, file_format_pattern_index):
        if not os.path.isfile(file_path):
            return

        self.__slice_file_path__(file_path)
        self.__convert_file_name_with_pattern__(file_path, file_format_pattern_index)
        new_file_path = self.__join_file_path__()

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
            return

        metadata_tags_dict = self.metadata_api.get_music_file_metadata(file_path)
        if not metadata_tags_dict:
            return

        if file_format_pattern_index == 0:
            self.file_name = '%s - %s' % \
                             (metadata_tags_dict['tracknumber'],
                              metadata_tags_dict['title'])
        elif file_format_pattern_index == 1:
            self.file_name = '%s. %s' % \
                             (metadata_tags_dict['tracknumber'],
                              metadata_tags_dict['title'])