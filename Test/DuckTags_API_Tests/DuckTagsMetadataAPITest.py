from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Test.Utils.DuckTagsTestMp3Tags import DuckTagsTestMp3Tags

import unittest
import mock


class DuckTagsMetadataAPITestCase(unittest.TestCase):

    def setUp(self):
        self.metadata_api = DuckTagsMetadataAPI()
        self.metadata_manager = self.metadata_api.metadata_manager

        self.mp3_file_path = 'folder/file_name.mp3'
        self.mp3_file_path_upper = 'folder/file_name.MP3'
        self.mp3_manager_index = 0

        self.invalid_music_file_name = 'file_name.xxx'

    def test_get_metadata_mp3_manager_index(self):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    def test_get_metadata_MP3_manager_index(self):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path_upper)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    def test_get_metadata_invalid_music_extension(self):
        self.metadata_api.get_music_file_metadata(self.invalid_music_file_name)

        self.assertRaises(IndexError)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3(self, mock_mutagen):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        mock_mutagen.assert_called_with(self.mp3_file_path)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags

        current_tags = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags, current_tags)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_title(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_title

        current_tags = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags_no_title, current_tags)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_album(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_album

        current_tags = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags_no_album, current_tags)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_genre(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_genre

        current_tags = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags_no_genre, current_tags)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_date(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_date

        current_tags = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags_no_date, current_tags)