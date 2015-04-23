import unittest

import Test.DuckTags_API_Tests.DuckTagsFileAPITests
import Test.DuckTags_API_Tests.DuckTagsMP3MetadataAPITest
import Test.DuckTags_API_Tests.DuckTagsFolderStructureAPITest

import Test.DuckTags_Src_Tests.DuckTagsFileNamesManagerTest
import Test.DuckTags_Src_Tests.DuckTagsDataBaseManagerTest


if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        test_loader.loadTestsFromTestCase(
            Test.DuckTags_API_Tests.DuckTagsFileAPITests.DuckTagsFileAPITestCase
        ),
        test_loader.loadTestsFromTestCase(
            Test.DuckTags_API_Tests.DuckTagsMP3MetadataAPITest.DuckTagsMP3MetadataAPITestCase
        ),
        test_loader.loadTestsFromTestCase(
            Test.DuckTags_API_Tests.DuckTagsFolderStructureAPITest.DuckTagsFolderStructureAPITestCase
        ),
        test_loader.loadTestsFromTestCase(
            Test.DuckTags_Src_Tests.DuckTagsFileNamesManagerTest.DuckTagsFileNamesManagerTestCase
        ),
        test_loader.loadTestsFromTestCase(
            Test.DuckTags_Src_Tests.DuckTagsDataBaseManagerTest.DuckTagsDataBaseManagerTestCase
        ),

    ))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)