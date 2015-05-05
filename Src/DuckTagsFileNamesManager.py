from Utils.DuckTagsExceptions import DuckTagsRenameException

import os


class DuckTagsFileManager(object):
    def __init__(self, tags_utils, metadata_api):
        self.utils = tags_utils
        self.metadata_api = metadata_api

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
        elif new_file_path == file_path:
            pass
        else:
            raise DuckTagsRenameException(file_path)

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

        music_file_model = self.metadata_api.get_music_file_metadata(file_path)

        track_number = music_file_model.tracknumber
        if len(track_number) == 1:
            track_number = '0%s' % track_number

        title = music_file_model.title

        if file_format_pattern_index == 0 or file_format_pattern_index == 1:
            self.file_name = self.utils.file_format_patterns[file_format_pattern_index][1] % (track_number, title)
        elif file_format_pattern_index == 2:
            pass

        return True