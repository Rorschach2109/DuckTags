from Src.DuckTagsDataBaseManager import DuckTagsDataBaseManager
from Test.TestUtils.DuckTagsTestDataBaseManagerUtils import DuckTagsTestDataBaseManagerUtils

import unittest
import mock


class DuckTagsDataBaseManagerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_manager = DuckTagsDataBaseManager()

        cls.music_files_dict_valid = DuckTagsTestDataBaseManagerUtils.music_files_dict_valid
        cls.music_files_dict_empty = DuckTagsTestDataBaseManagerUtils.music_files_dict_empty
        cls.music_files_directories_valid = DuckTagsTestDataBaseManagerUtils.music_files_directories_valid
        cls.music_file_model = DuckTagsTestDataBaseManagerUtils.music_file_model
        cls.music_files_dict = DuckTagsTestDataBaseManagerUtils.music_files_dict
        cls.valid_first_mp3_tags = DuckTagsTestDataBaseManagerUtils.valid_first_mp3_tags
        cls.valid_second_mp3_tags = DuckTagsTestDataBaseManagerUtils.valid_second_mp3_tags
        cls.first_music_file_model = DuckTagsTestDataBaseManagerUtils.first_music_file_model
        cls.second_music_file_model = DuckTagsTestDataBaseManagerUtils.second_music_file_model

    def test_get_music_file_path_valid(self):
        music_files_directories = list(DuckTagsDataBaseManager.__get_music_file_path__(self.music_files_dict_valid))
        self.assertListEqual(self.music_files_directories_valid, music_files_directories)

    def test_get_music_file_path_empty_dict(self):
        music_files_directories = list(DuckTagsDataBaseManager.__get_music_file_path__(self.music_files_dict_empty))
        self.assertListEqual([], music_files_directories)

    @mock.patch('Src.DuckTagsDataBaseManager.Database.insert')
    @mock.patch('Src.DuckTagsDataBaseManager.Database.get')
    def test_insert_music_file_model_existing_element(self, mock_db_get, mock_db_insert):
        mock_db_get.return_value = None
        mock_db_insert.return_value = None

        self.db_manager.__insert_music_file_model__(self.music_file_model)

        self.assertFalse(mock_db_insert.called)

    @mock.patch('Src.DuckTagsDataBaseManager.Database.get')
    @mock.patch('DuckTags_API.DuckTagsMetadataAPI.DuckTagsMetadataAPI')
    def test_insert_music_file(self, mock_metadata_api, mock_db_get):
        mock_metadata_api.get_music_file_metadata.side_effects = [
            self.valid_first_mp3_tags,
            self.valid_second_mp3_tags,
            ]

        mock_db_get.return_value = None
        self.db_manager.__insert_music_files_to_db__(self.music_files_dict)

        calls = [
            mock.call('path', self.first_music_file_model.path),
            mock.call('path', self.second_music_file_model.path)
        ]

        mock_db_get.assert_has_calls(calls)
