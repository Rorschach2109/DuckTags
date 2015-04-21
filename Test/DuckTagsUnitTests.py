import unittest

import DuckTags_API_Tests.DuckTagsFileAPITests
import DuckTags_API_Tests.DuckTagsMP3MetadataAPITest
import DuckTags_API_Tests.DuckTagsFolderStructureAPITest
import DuckTags_API_Tests.DuckTagsFolderStructureManagerTest


if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        test_loader.loadTestsFromTestCase(
            DuckTags_API_Tests.DuckTagsFileAPITests.DuckTagsFileAPITestCase
        ),
        test_loader.loadTestsFromTestCase(
            DuckTags_API_Tests.DuckTagsMP3MetadataAPITest.DuckTagsMP3MetadataAPITestCase
        ),
        test_loader.loadTestsFromTestCase(
            DuckTags_API_Tests.DuckTagsFolderStructureAPITest.DuckTagsFolderStructureAPITestCase
        ),
        test_loader.loadTestsFromTestCase(
            DuckTags_API_Tests.DuckTagsFolderStructureManagerTest.DuckTagsFolderStructureManagerTestCase
        ),
    ))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)