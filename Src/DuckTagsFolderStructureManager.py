from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Utils.DuckTagsUtils import DuckTagsUtils
from Src.DuckTagsFileNamesManager import DuckTagsFileManager


class DuckTagsFolderStructureManager(object):
    def __init__(self):
        utils = DuckTagsUtils()
        metadata_api = DuckTagsMetadataAPI()
        self.file_manager = DuckTagsFileManager(utils, metadata_api)

    def get_available_files_format_patterns(self):
        return self.file_manager.get_available_files_format_patterns()

    def reorganize_files_with_pattern(self, files_paths_list, file_format_pattern_index):
        return self.file_manager.reorganize_files_with_pattern(files_paths_list, file_format_pattern_index)