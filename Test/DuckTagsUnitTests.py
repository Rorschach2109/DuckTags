import unittest

import DuckTags_API_Tests.DuckTagsFileAPITests


if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        test_loader.loadTestsFromTestCase(DuckTags_API_Tests.DuckTagsFileAPITests.DuckTagsFileAPITestCase)
    ))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)