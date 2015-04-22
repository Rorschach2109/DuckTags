from Src.DuckTagsFolderStructureManager import DuckTagsFolderStructureManager


class DuckTagsFolderStructureAPI(object):
    def __init__(self):
        self.folder_structure_manager = DuckTagsFolderStructureManager()

    def get_available_files_format_patterns(self):
        return self.folder_structure_manager.get_available_files_format_patterns()

    def reorganize_files_with_pattern(self, files_paths_list, file_format_pattern_index):
        return self.folder_structure_manager.reorganize_files_with_pattern(files_paths_list, file_format_pattern_index)