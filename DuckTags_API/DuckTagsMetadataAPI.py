from Src.DuckTagsMetadataManager import DuckTagsMetadataManager


class DuckTagsMetadataAPI(object):
    def __init__(self):
        self.metadata_manager = DuckTagsMetadataManager()

    def get_music_file_metadata(self, music_file_path):
        return self.metadata_manager.get_music_file_metadata(music_file_path)

    def get_music_files_list_metadata(self, music_files_paths_list):
        return self.metadata_manager.get_music_files_list_metadata(music_files_paths_list)

    def set_music_file_metadata(self, music_file_path, music_metadata_dict):
        return self.metadata_manager.set_music_file_metadata(music_file_path, music_metadata_dict)

    def set_music_file_list_metadata(self, music_files_paths_list, music_metadata_dict):
        return self.metadata_manager.set_music_file_list_metadata(music_files_paths_list, music_metadata_dict)

    def set_music_file_metadata_uppercase(self, music_file_path):
        return self.metadata_manager.set_music_file_metadata_uppercase(music_file_path)

    def set_music_file_list_metadata_uppercase(self, music_files_paths_list):
        return self.metadata_manager.set_music_file_list_metadata_uppercase(music_files_paths_list)

    def get_music_files_list_cover(self, music_files_paths_list):
        return self.metadata_manager.get_music_files_list_cover(music_files_paths_list)
