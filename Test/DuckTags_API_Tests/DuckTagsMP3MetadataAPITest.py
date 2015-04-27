from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Src.DuckTagsDatabaseTools.DuckTagsMusicFileModel import DuckTagsMusicFileModel
from Test.TestUtils.DuckTagsTestMp3Tags import DuckTagsTestMp3Tags
from Test.TestUtils.DuckTagsTestMp3Mocks import DuckTagsMP3AudioMock

import unittest
import mock


class DuckTagsMP3MetadataAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.metadata_api = DuckTagsMetadataAPI()
        cls.metadata_manager = cls.metadata_api.metadata_manager

        cls.mp3_file_path = 'folder/file_name.mp3'
        cls.mp3_files_paths_list = ['file_name.mp3', 'file_name.mp3', 'file_name.mp3']

        cls.mp3_file_path_upper = 'folder/file_name.MP3'
        cls.mp3_manager_index = 0

        cls.invalid_music_file_path = 'file_name.xxx'
        cls.invalid_music_files_paths_list = ['file_name.mp3', 'file_name.xxx']

        cls.multiple_values_text = u'Multiple Values'

    def test_get_metadata_mp3_manager_index(self):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    def test_get_metadata_MP3_manager_index(self):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path_upper)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    def test_get_metadata_invalid_music_extension(self):
        current_metadata = self.metadata_api.get_music_file_metadata(self.invalid_music_file_path)

        self.assertRaises(TypeError)
        self.assertIsNone(current_metadata)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3(self, mock_mutagen):
        self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        mock_mutagen.assert_called_with(self.mp3_file_path)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags

        expected_music_file_model = DuckTagsMusicFileModel(self.mp3_file_path,
                                                           DuckTagsTestMp3Tags.valid_mp3_tags)
        current_music_file_model = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_title(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_title

        expected_music_file_model = DuckTagsMusicFileModel(self.mp3_file_path,
                                                           DuckTagsTestMp3Tags.valid_mp3_tags_no_title)
        current_music_file_model = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_album(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_album

        expected_music_file_model = DuckTagsMusicFileModel(self.mp3_file_path,
                                                           DuckTagsTestMp3Tags.valid_mp3_tags_no_album)
        current_music_file_model = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_genre(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_genre

        expected_music_file_model = DuckTagsMusicFileModel(self.mp3_file_path,
                                                           DuckTagsTestMp3Tags.valid_mp3_tags_no_genre)
        current_music_file_model = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_mp3_valid_tags_no_date(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags_no_date

        expected_music_file_model = DuckTagsMusicFileModel(self.mp3_file_path,
                                                           DuckTagsTestMp3Tags.valid_mp3_tags_no_date)
        current_music_file_model = self.metadata_api.get_music_file_metadata(self.mp3_file_path)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    def test_get_metadata_list_mp3_manager_index(self):
        self.metadata_api.get_music_files_list_metadata(self.mp3_files_paths_list)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    def test_get_metadata_list_invalid_music_extension(self):
        current_metadata = self.metadata_api.get_music_files_list_metadata(self.invalid_music_files_paths_list)

        self.assertRaises(TypeError)
        self.assertIsNone(current_metadata)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_list_mp3(self, mock_mutagen):
        self.metadata_api.get_music_files_list_metadata(self.mp3_files_paths_list)

        mock_mutagen.assert_called_with(self.mp3_files_paths_list[0])
        mock_mutagen.assert_called_with(self.mp3_files_paths_list[1])
        mock_mutagen.assert_called_with(self.mp3_files_paths_list[2])

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_list_mp3_valid_tags(self, mock_mutagen):
        mock_mutagen.side_effect = [
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags,
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags,
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags
        ]

        expected_music_file_model = DuckTagsMusicFileModel(self.multiple_values_text,
                                                           DuckTagsTestMp3Tags.valid_mp3_tags)
        current_music_file_model = self.metadata_api.get_music_files_list_metadata(self.mp3_files_paths_list)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_list_mp3_valid_tags_diff_titles(self, mock_mutagen):
        mock_mutagen.side_effect = [
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags,
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags,
            DuckTagsTestMp3Tags.valid_mp3_second_mutagen_tags
        ]

        expected_music_file_model = DuckTagsMusicFileModel(self.multiple_values_text,
                                                           DuckTagsTestMp3Tags.valid_mp3_multi_files_tags)
        current_music_file_model = self.metadata_api.get_music_files_list_metadata(self.mp3_files_paths_list)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_get_metadata_list_mp3_valid_tags_diff_whole(self, mock_mutagen):
        mock_mutagen.side_effect = [
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags,
            DuckTagsTestMp3Tags.valid_mp3_mutagen_tags,
            DuckTagsTestMp3Tags.valid_mp3_mutagen_empty_tags
        ]

        expected_music_file_model = DuckTagsMusicFileModel(self.multiple_values_text,
                                                           DuckTagsTestMp3Tags.valid_mp3_multi_values_files_tags)
        current_music_file_model = self.metadata_api.get_music_files_list_metadata(self.mp3_files_paths_list)

        self.assertDictEqual(expected_music_file_model.serialize(), current_music_file_model.serialize())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_mp3_manager_index(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsMP3AudioMock()

        self.metadata_api.set_music_file_metadata(self.mp3_file_path, DuckTagsTestMp3Tags.valid_mp3_different_tags)

        current_manager_index = self.metadata_manager.metadata_manager_index

        self.assertEqual(self.mp3_manager_index, current_manager_index)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_mp3_invalid_music_extension(self, mock_mutagen):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_mutagen.return_value = mp3_audio_mock

        self.metadata_api.set_music_file_metadata(self.invalid_music_file_path,
                                                  DuckTagsTestMp3Tags.valid_mp3_different_tags)

        self.assertRaises(TypeError)
        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags, mp3_audio_mock.get_tags_dict())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_mp3_valid_music_extension(self, mock_mutagen):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_mutagen.return_value = mp3_audio_mock

        self.metadata_api.set_music_file_metadata(self.mp3_file_path,
                                                  DuckTagsTestMp3Tags.valid_mp3_different_tags)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_different_tags, mp3_audio_mock.get_tags_dict())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_mp3_empty_tags_dict(self, mock_mutagen):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_mutagen.return_value = mp3_audio_mock

        self.metadata_api.set_music_file_metadata(self.mp3_file_path,
                                                  DuckTagsTestMp3Tags.invalid_mp3_empty_tags)

        self.assertDictEqual(DuckTagsTestMp3Tags.valid_mp3_tags, mp3_audio_mock.get_tags_dict())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_mp3_mutagen_exception(self, mock_mutagen):
        mock_mutagen.side_effect = Exception

        self.metadata_api.set_music_file_metadata(self.mp3_file_path,
                                                  DuckTagsTestMp3Tags.invalid_mp3_empty_tags)

        self.assertRaises(Exception())

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_list_mp3_manager_index(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsMP3AudioMock()

        self.metadata_api.set_music_file_list_metadata(self.mp3_files_paths_list, DuckTagsTestMp3Tags.valid_mp3_tags)

        current_manager_index = self.metadata_manager.metadata_manager_index
        self.assertEqual(self.mp3_manager_index, current_manager_index)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_set_metadata_mp3_list_invalid_music_extension(self, mock_mutagen):
        mock_mutagen.return_value = DuckTagsMP3AudioMock()

        self.metadata_api.set_music_file_list_metadata(self.invalid_music_files_paths_list,
                                                       DuckTagsTestMp3Tags.valid_mp3_tags)
        self.assertRaises(TypeError)