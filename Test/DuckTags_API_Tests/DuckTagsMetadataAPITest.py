from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI

import unittest
import mock


class DuckTagsMetadataAPITestCase(unittest.TestCase):

    def setUp(self):
        self.metadata_api = DuckTagsMetadataAPI()
        self.metadata_manager = self.metadata_api.metadata_manager

        self.mp3_file_path = 'folder/file_name.mp3'
        self.mp3_manager_index = 0

        self.invalid_music_file_name = 'file_name.xxx'

    def test_get_metadata_mp3_manager_index(self):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    def test_get_metadata_invalid_music_extension(self):
        self.metadata_api.get_music_file_metadata(self.invalid_music_file_name)

        self.assertRaises(IndexError)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3(self, mock_mutagen):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        mock_mutagen.assert_called_with(self.mp3_file_path)