from Src.DuckTagsMetadataManager import DuckTagsMetadataManager


class DuckTagsMetadataAPI(object):
    def __init__(self):
        self.metadata_manager = DuckTagsMetadataManager()

    def get_music_file_metadata(self, music_file_path):
        return self.metadata_manager.get_music_file_metadata(music_file_path)

    def get_music_files_list_metadata(self, music_files_paths_list):
        return self.metadata_manager.get_music_files_list_metadata(music_files_paths_list)
