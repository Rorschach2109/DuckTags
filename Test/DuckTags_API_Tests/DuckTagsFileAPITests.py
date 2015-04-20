from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI

import unittest
import mock


class DuckTagsFileAPITestCase(unittest.TestCase):

    def setUp(self):
        self.file_api = DuckTagsFileAPI()
        self.file_manager = self.file_api.file_manager

        self.music_extensions_list = ['mp3', 'wav', 'ogg']
        self.doubled_music_extensions_list = ['mp3', 'wav', 'ogg', 'wav', 'ogg', 'mp3']
        self.empty_music_extensions_list = []

        self.folder_path = 'folder_path'

        self.files_dict = {
            'folder_path_1': ['1.mp3', '2.jpg', '3.ogg'],
            'folder_path_2': [],
            'folder_path_3': ['1.jpg', '2.bmp', '3.txt'],
            'folder_path_4': ['1.doc', '2.mp3', '3.ogg', '4.wav']
        }

        self.music_files_dict = {
            'folder_path_1': ['1.mp3', '3.ogg'],
            'folder_path_2': [],
            'folder_path_3': [],
            'folder_path_4': ['2.mp3', '3.ogg', '4.wav']
        }

        self.empty_music_files_dict = {
            'folder_path_1': [],
            'folder_path_2': [],
            'folder_path_3': [],
            'folder_path_4': []
        }

    def test_get_music_files(self):
        current_music_files_dict = self.file_api.get_music_files_from_files_dict(self.files_dict,
                                                                                 self.music_extensions_list)
        self.assertDictEqual(self.music_files_dict, current_music_files_dict)

    def test_get_music_files_empty_extensions_list(self):
        current_music_files_dict = self.file_api.get_music_files_from_files_dict(self.files_dict,
                                                                                 self.empty_music_extensions_list)
        self.assertDictEqual(self.empty_music_files_dict, current_music_files_dict)

    def test_get_music_files_check_extensions_list(self):
        self.file_api.get_music_files_from_files_dict(self.files_dict, self.doubled_music_extensions_list)

        current_extensions_list = self.file_manager.music_extensions_list

        self.assertListEqual(sorted(self.music_extensions_list), sorted(current_extensions_list))

    def test_get_files_dict_current_path(self):
        self.file_api.get_files_dict_from_folder(self.folder_path)

        current_folder_path = self.file_manager.current_folder_path

        self.assertEqual(self.folder_path, current_folder_path)

    @mock.patch('Src.DuckTagsFileManager.os')
    def test_get_files_dict(self, mock_os):
        self.file_api.get_files_dict_from_folder(self.folder_path)
        mock_os.walk.assert_called_with(self.folder_path)

    @mock.patch('Src.DuckTagsFileManager.os')
    def test_get_files_dict_empty_walk(self, mock_os):
        mock_os.walk.return_value = ()
        current_files_dict = self.file_api.get_files_dict_from_folder(self.folder_path)

        self.assertDictEqual({}, current_files_dict)

    @mock.patch('Src.DuckTagsFileManager.os')
    def test_get_files_dict_valid_walk(self, mock_os):
        walk_mock_generator = ((folder_name, [], self.files_dict[folder_name]) for folder_name in self.files_dict)
        mock_os.walk.return_value = walk_mock_generator

        current_files_dict = self.file_api.get_files_dict_from_folder(self.folder_path)

        self.assertDictEqual(self.files_dict, current_files_dict)