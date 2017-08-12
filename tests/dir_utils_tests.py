import types
import unittest
from utilbox.os_utils import DirUtils


class DirUtilsTest(unittest.TestCase):
    """
    Base class for all tests, which defined common 'setUp' and 'tearDown' methods.
    """

    def setUp(self):
        """
        Prepare environment to run automated tests.
        """

        import os

        self.test_data_root = "test_data"
        self.test_dirs = [os.path.normpath(self.test_data_root + "/" + "dir1"),
                          os.path.normpath(self.test_data_root + "/" + "dir2")]
        self.test_files = ["file1.txt", "file2.txt", "file3.log", "file4.log"]

        for test_dir in self.test_dirs:
            if not os.path.exists(test_dir):
                os.makedirs(test_dir)

            for test_file_name in self.test_files:
                test_file = open(os.path.normpath(test_dir + "/" + test_file_name), "w+")
                test_file.write("This is the content for " + str(test_file_name) + ".")

    def tearDown(self):
        """
        Restore environment to pre-test conditions.
        """

        import shutil
        shutil.rmtree(self.test_data_root)


class DirUtilsTestInit(DirUtilsTest):
    """
    Class for testing various aspects of instantiation.
    """

    pass


class DirUtilsTestSetter(DirUtilsTest):
    """
    Class for testing various aspects of setting attributes.
    """

    pass


class DirUtilsTestMethodInput(DirUtilsTest):
    """
    Class for testing methods taking input parameters.
    """

    pass


class DirUtilsTestMethodReturnType(DirUtilsTest):
    """
    Class for testing return types of all methods.
    """

    def test_get_dir_entries(self):
        """
        Test if returned value is a list.
        """

        test_file_extensions = ["pdf"]

        for test_directory in self.test_dirs:
            for test_file_extension in test_file_extensions:
                self.assertIsInstance(DirUtils.get_dir_contents(test_directory, test_file_extension),
                                      types.ListType)


class DirUtilsTestMethodReturnValue(DirUtilsTest):
    """
    Class for testing return values of all methods against known values.
    """

    pass


if __name__ == '__main__':
    unittest.main()
