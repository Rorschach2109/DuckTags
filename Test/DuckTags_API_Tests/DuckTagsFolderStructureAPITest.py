import unittest
import mock

from DuckTags_API.DuckTagsFolderStructureAPI import DuckTagsFolderStructureAPI
from Utils.DuckTagsUtils import DuckTagsUtils
from Test.TestUtils.DuckTagsTestMp3Tags import DuckTagsTestMp3Tags


class DuckTagsFolderStructureAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.folder_structure_api = DuckTagsFolderStructureAPI()
        cls.utils = DuckTagsUtils()

        cls.file_path = r'/home/directory/Folder/file_name.mp3'
        cls.reorganized_file_path_1 = r'/home/directory/Folder/%s - %s' % \
                                      (DuckTagsTestMp3Tags.valid_mp3_tags[u'tracknumber'],
                                       DuckTagsTestMp3Tags.valid_mp3_tags[u'title'])

    def test_get_files_format_patterns(self):
        files_patterns = self.folder_structure_api.get_available_files_format_patterns()

        self.assertListEqual(self.utils.file_format_patterns, files_patterns)

    @mock.patch('Src.DuckTagsMp3MetadataManager.EasyID3')
    @mock.patch('Src.DuckTagsFolderStructureManager.os')
    def test_reorganize_files_with_pattern_1(self, mock_mutagen, mock_os):
        mock_mutagen.return_value = DuckTagsTestMp3Tags.valid_mp3_mutagen_tags

        self.folder_structure_api.reorganize_files_with_pattern([self.file_path],
                                                                self.utils.file_format_patterns[0])

        mock_os.rename.assert_called_with(self.file_path, self.reorganized_file_path_1)