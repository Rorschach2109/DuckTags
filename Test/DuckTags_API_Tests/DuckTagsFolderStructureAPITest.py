import unittest
import mock

from DuckTags_API.DuckTagsFolderStructureAPI import DuckTagsFolderStructureAPI
from Utils.DuckTagsUtils import DuckTagsUtils
from Test.TestUtils.DuckTagsTestMp3Tags import DuckTagsTestMp3Tags
from Test.TestUtils.DuckTagsTestMp3Mocks import DuckTagsMP3AudioMock


class DuckTagsFolderStructureAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.folder_structure_api = DuckTagsFolderStructureAPI()
        cls.utils = DuckTagsUtils()

        cls.file_path = u'/home/directory/Folder/file_name.mp3'
        cls.reorganized_file_path_1 = u'/home/directory/Folder/%s - %s' % \
                                      (DuckTagsTestMp3Tags.valid_mp3_tags[u'tracknumber'],
                                       DuckTagsTestMp3Tags.valid_mp3_tags[u'title'])

    def test_get_files_format_patterns(self):
        files_patterns = self.folder_structure_api.get_available_files_format_patterns()

        self.assertListEqual(self.utils.file_format_patterns, files_patterns)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    @mock.patch('os.path.isfile')
    @mock.patch('os.rename')
    def test_reorganize_files_with_pattern_1(self, mock_os_rename, mock_os_isfile, mock_metadata):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_metadata.return_value = mp3_audio_mock
        mock_os_isfile.return_value = True

        self.folder_structure_api.reorganize_files_with_pattern([self.file_path], 0)
        reorganized_file_path = u'/home/directory/Folder/%s - %s.mp3' % \
                                (mp3_audio_mock[u'tracknumber'][0],
                                 mp3_audio_mock[u'title'][0])

        mock_os_rename.assert_called_once_with(self.file_path, reorganized_file_path)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    @mock.patch('os.path.isfile')
    @mock.patch('os.rename')
    def test_reorganize_files_with_pattern_2(self, mock_os_rename, mock_os_isfile, mock_metadata):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_metadata.return_value = mp3_audio_mock
        mock_os_isfile.return_value = True

        self.folder_structure_api.reorganize_files_with_pattern([self.file_path], 1)
        reorganized_file_path = u'/home/directory/Folder/%s. %s.mp3' % \
                                (mp3_audio_mock[u'tracknumber'][0],
                                 mp3_audio_mock[u'title'][0])

        mock_os_rename.assert_called_once_with(self.file_path, reorganized_file_path)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    @mock.patch('os.path.isfile')
    @mock.patch('os.rename')
    def test_reorganize_files_with_pattern_false_isfile(self, mock_os_rename, mock_os_isfile, mock_metadata):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_metadata.return_value = mp3_audio_mock
        mock_os_isfile.return_value = False

        self.folder_structure_api.reorganize_files_with_pattern([self.file_path], 1)

        self.assertFalse(mock_os_rename.called)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    @mock.patch('os.path.isfile')
    @mock.patch('os.rename')
    def test_reorganize_files_with_pattern_invalid_pattern_index(self, mock_os_rename, mock_os_isfile, mock_metadata):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mock_metadata.return_value = mp3_audio_mock
        mock_os_isfile.return_value = True

        self.folder_structure_api.reorganize_files_with_pattern([self.file_path], 10)

        self.assertFalse(mock_os_rename.called)

    @mock.patch('Src.DuckTagsMp3MetadataManager.DuckTagsMp3MetadataManager.get_music_file_metadata')
    @mock.patch('os.path.isfile')
    @mock.patch('os.rename')
    def test_reorganize_files_with_pattern_empty_tags(self, mock_os_rename, mock_os_isfile, mock_metadata):
        mp3_audio_mock = DuckTagsMP3AudioMock()
        mp3_audio_mock.clear_tags()
        mock_metadata.return_value = {}
        mock_os_isfile.return_value = True

        self.folder_structure_api.reorganize_files_with_pattern([self.file_path], 1)

        self.assertFalse(mock_os_rename.called)