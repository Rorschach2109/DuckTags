from Src.DuckTagsDataBaseManager import DuckTagsDataBaseManager
from Test.TestUtils.DuckTagsTestDataBaseManagerUtils import DuckTagsTestDataBaseManagerUtils

import unittest
import mock


class DuckTagsDataBaseManagerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_manager = DuckTagsDataBaseManager()

        cls.files_dict_valid = DuckTagsTestDataBaseManagerUtils.files_dict_valid
        cls.music_files_dict_valid = DuckTagsTestDataBaseManagerUtils.music_files_dict_valid
        cls.music_files_dict_empty = DuckTagsTestDataBaseManagerUtils.music_files_dict_empty
        cls.music_files_directories_valid = DuckTagsTestDataBaseManagerUtils.music_files_directories_valid
        cls.music_file_model = DuckTagsTestDataBaseManagerUtils.music_file_model
        cls.music_files_dict = DuckTagsTestDataBaseManagerUtils.music_files_dict
        cls.valid_first_mp3_tags = DuckTagsTestDataBaseManagerUtils.valid_first_mp3_tags
        cls.valid_second_mp3_tags = DuckTagsTestDataBaseManagerUtils.valid_second_mp3_tags
        cls.first_music_file_model = DuckTagsTestDataBaseManagerUtils.first_music_file_model
        cls.second_music_file_model = DuckTagsTestDataBaseManagerUtils.second_music_file_model
        cls.music_file_model_no_album = DuckTagsTestDataBaseManagerUtils.music_file_model_no_album
        cls.first_music_file_model_serialization = \
            DuckTagsTestDataBaseManagerUtils.first_music_file_model_serialization
        cls.second_music_file_model_serialization = \
            DuckTagsTestDataBaseManagerUtils.second_music_file_model_serialization
        cls.music_file_model_serialization_no_album = \
            DuckTagsTestDataBaseManagerUtils.music_file_model_serialization_no_album

    def setUp(self):
        self.db_manager.db_indexes = []

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

    @mock.patch('Src.DuckTagsDataBaseManager.Database.add_index')
    @mock.patch('Src.DuckTagsDataBaseManager.Database.create')
    @mock.patch('Src.DuckTagsDataBaseManager.Database.get')
    @mock.patch('DuckTags_API.DuckTagsMetadataAPI.DuckTagsMetadataAPI')
    def test_insert_music_file(self, mock_metadata_api, mock_db_get, mock_db_create, mock_db_add_index):
        mock_metadata_api.get_music_file_metadata.side_effects = [
            self.valid_first_mp3_tags,
            self.valid_second_mp3_tags,
            ]

        mock_db_get.return_value = None
        mock_db_create.return_value = None
        mock_db_add_index.return_value = None

        self.db_manager.db_indexes = range(10)
        self.db_manager.__insert_music_files_to_db__(self.music_files_dict)

        calls = [
            mock.call('path', self.first_music_file_model.path),
            mock.call('path', self.second_music_file_model.path)
        ]

        mock_db_get.assert_has_calls(calls)

    @mock.patch('DuckTags_API.DuckTagsFileAPI.DuckTagsFileAPI.get_music_files_from_files_dict')
    @mock.patch('DuckTags_API.DuckTagsFileAPI.DuckTagsFileAPI.get_files_dict_from_folder')
    def test_get_music_file_from_folder(self, mock_get_files_dict, mock_get_music_files_dict):
        mock_get_files_dict.return_value = self.files_dict_valid
        mock_get_music_files_dict.return_value = self.music_files_dict_valid

        music_files = self.db_manager.__get_music_files_from_folder__(u'')

        self.assertDictEqual(self.music_files_dict_valid, music_files)

    def test_music_file_serialization(self):
        serialization_data = self.first_music_file_model.serialize()
        self.assertDictEqual(self.first_music_file_model_serialization, serialization_data)

    def test_music_file_serialization_no_album(self):
        serialization_data = self.music_file_model_no_album.serialize()
        self.assertDictEqual(self.music_file_model_serialization_no_album, serialization_data)

    @mock.patch('Src.DuckTagsDataBaseManager.Database.delete')
    @mock.patch('Src.DuckTagsDataBaseManager.Database.all')
    def test_clean_db(self, mock_db_all, mock_db_delete):
        mock_db_all.return_value = range(10)
        mock_db_delete.return_value = None

        self.db_manager.__clean_db__()

        calls = [mock.call(element) for element in range(10)]
        mock_db_delete.assert_has_calls(calls)

    @mock.patch('Src.DuckTagsDataBaseManager.Database.delete')
    @mock.patch('Src.DuckTagsDataBaseManager.Database.all')
    def test_clean_db_no_elements(self, mock_db_all, mock_db_delete):
        mock_db_all.return_value = []
        mock_db_delete.return_value = None

        self.db_manager.__clean_db__()

        self.assertFalse(mock_db_delete.called)

    @mock.patch('Src.DuckTagsDataBaseManager.Database.destroy_index')
    def test_clean_indexes(self, mock_destroy_index):
        mock_destroy_index.return_value = None
        self.db_manager.db_indexes = range(10)

        self.db_manager.__clean_indexes__()

        calls = [mock.call(index) for index in range(10)]
        mock_destroy_index.assert_has_calls(calls)

    @mock.patch('Src.DuckTagsDataBaseManager.Database.destroy_index')
    def test_clean_indexes_no_indexes(self, mock_destroy_index):
        mock_destroy_index.return_value = None

        self.db_manager.__clean_indexes__()

        self.assertFalse(mock_destroy_index.called)