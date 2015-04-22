from Src.DuckTagsFileNamesManager import DuckTagsFileManager
from Test.TestUtils.DuckTagsTestMp3Tags import DuckTagsTestMp3Tags
from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Utils.DuckTagsUtils import DuckTagsUtils

import unittest
import mock


class DuckTagsFileNamesManagerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils = DuckTagsUtils()
        metadata_api = DuckTagsMetadataAPI()
        cls.file_manager = DuckTagsFileManager(utils, metadata_api)
        cls.test_mp3_tags = DuckTagsTestMp3Tags()

        cls.file_path = '/home/test_directory/file.mp3'
        cls.file_path_root = '/home/test_directory/'
        cls.file_name = 'file'
        cls.file_extension = '.mp3'

    def test_slice_file_path_file_path_root(self):
        self.file_manager.__slice_file_path__(self.file_path)

        current_file_path_root = self.file_manager.file_path_root

        self.assertEqual(self.file_path_root, current_file_path_root)

    def test_slice_file_path_file_name(self):
        self.file_manager.__slice_file_path__(self.file_path)

        current_file_name = self.file_manager.file_name

        self.assertEqual(self.file_name, current_file_name)

    def test_slice_file_path_file_extension(self):
        self.file_manager.__slice_file_path__(self.file_path)

        current_file_extension = self.file_manager.file_extension

        self.assertEqual(self.file_extension, current_file_extension)

    def test_join_file_path(self):
        self.file_manager.file_path_root = self.file_path_root
        self.file_manager.file_name = self.file_name
        self.file_manager.file_extension = self.file_extension

        current_joined_file_path = self.file_manager.__join_file_path__()

        self.assertEqual(self.file_path, current_joined_file_path)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_convert_file_name_with_pattern_1(self, mock_mutagen):
        self.file_manager.file_name = self.file_name

        mock_mutagen.return_value = self.test_mp3_tags.valid_mp3_second_mutagen_tags

        self.file_manager.__convert_file_name_with_pattern__(self.file_path, 0)

        current_file_name = self.file_manager.file_name
        expected_file_name = '%s - %s' % \
                             (self.test_mp3_tags.valid_mp3_second_mutagen_tags['tracknumber'][0],
                              self.test_mp3_tags.valid_mp3_second_mutagen_tags['title'][0])

        self.assertEqual(expected_file_name, current_file_name)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    def test_convert_file_name_with_pattern_2(self, mock_mutagen):
        self.file_manager.file_name = self.file_name

        mock_mutagen.return_value = self.test_mp3_tags.valid_mp3_second_mutagen_tags

        self.file_manager.__convert_file_name_with_pattern__(self.file_path, 1)

        current_file_name = self.file_manager.file_name
        expected_file_name = '%s. %s' % \
                             (self.test_mp3_tags.valid_mp3_second_mutagen_tags['tracknumber'][0],
                              self.test_mp3_tags.valid_mp3_second_mutagen_tags['title'][0])

        self.assertEqual(expected_file_name, current_file_name)