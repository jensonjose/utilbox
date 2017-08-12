"""
Utility module to manipulate directories.
"""

import os
import types
import shutil

__author__ = "Jenson Jose"
__email__ = "jensonjose@live.in"
__status__ = "Alpha"


class DirUtils:
    """
    Utility class containing methods to manipulate directories.
    """

    def __init__(self):
        pass

    @staticmethod
    def create_dir(dir_path):
        """
        Creates a directory at the specified path.

        :param dir_path: The full path of the directory to be created.

        :return: True, if directory was created, False otherwise.
        :rtype: bool
        """

        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                return True

            return False
        except Exception as ex:
            return False

    @staticmethod
    def create_dir_path_string(path_components, separator="/"):
        """
        Combines list of supplied path components to create a full directory path.

        :param path_components: List of components to be part of the final directory path.
        :param separator: Separator to be used for isolating directory path components.

        :return: The full directory path string, if path_components is a valid list, False otherwise.
        :rtype: str
        """

        if isinstance(path_components, types.ListType):
            if len(path_components) > 0:
                path_string = ""

                for component in path_components:
                    path_string += component + separator

                path_string = path_string[:-1]
                path_string = os.path.normpath(path_string)

                return path_string

        return False

    @staticmethod
    def fix_path(path1, path2):
        """
        Combines 2 given paths to form OS compliant path with correct path separators.

        Example:
            1st path (Linux): /root/some_dir; 2nd path (Windows): \test\data
            After combining the above paths,
                On Windows: \root\some_dir\test\data
                On Linux: /root/some_dir/test/data

        :param path1: The first path to be combined.
        :param path2: The second path to be combined.

        :return: The final combined path.
        :rtype: str
        """

        return os.path.normpath(path1 + path2)

    @staticmethod
    def check_valid_dir(dir_path):
        """
        Verifies if given directory path exists and is a valid directory.

        :param dir_path: The full path of the directory to be verified.

        :return: True if path contains a valid directory, False otherwise.
        :rtype: bool
        """

        if os.path.exists(dir_path):
            if os.path.isdir(dir_path):
                return True

        return False

    @staticmethod
    def create_archive(output_file_name, source_path, archive_format="zip"):
        """
        Creates a compressed archive of the specified directory.

        :param output_file_name: Name of the output archive file.
        :param source_path: The full path of the source to be archived.
        :param archive_format: The format to be used for archiving, and can be either ZIP, TAR, BZTAR or GZTAR.

        :return: True if archiving was successful, False otherwise.
        :rtype: bool
        """

        if shutil.make_archive(output_file_name, archive_format.lower(), source_path):
            return True

        return False

    @staticmethod
    def get_dir_contents(source_dir, filter_pattern=None, meta_data=False):
        """
        Returns a list of directory contents matching the supplied search pattern.

        If no pattern is supplied all directory contents are returned.

        :param source_dir: The path of the directory to be searched.
        :param filter_pattern: The pattern to be used to search the directory.
        :param meta_data: If True, returns a list of dictionaries containing meta data of each individual entry.

        :return: List of matching entries if the directory is valid, False otherwise.
        :rtype: list
        """

        from utilbox.os_utils import FileUtils

        filtered_entry_list = []

        if DirUtils.check_valid_dir(source_dir):
            dir_entries = os.listdir(source_dir)

            for dir_entry in dir_entries:
                if filter_pattern is not None:
                    import re

                    compiled_pattern = re.compile(filter_pattern)
                    if len(compiled_pattern.findall(dir_entry)) > 0:
                        if meta_data:
                            dir_entry_path = DirUtils.create_dir_path_string([source_dir,
                                                                              dir_entry])

                            if DirUtils.check_valid_dir(dir_entry_path):
                                meta_data = DirUtils.get_dir_metadata(dir_entry_path)
                            elif FileUtils.check_valid_file(dir_entry_path):
                                meta_data = FileUtils.get_file_metadata(dir_entry_path)

                            if meta_data:
                                filtered_entry_list.append(meta_data)
                        else:
                            filtered_entry_list.append(dir_entry)
                else:
                    if meta_data:
                        dir_entry_path = DirUtils.create_dir_path_string([source_dir,
                                                                          dir_entry])

                        if DirUtils.check_valid_dir(dir_entry_path):
                            meta_data = DirUtils.get_dir_metadata(dir_entry_path)
                        elif FileUtils.check_valid_file(dir_entry_path):
                            meta_data = FileUtils.get_file_metadata(dir_entry_path)

                        if meta_data:
                            filtered_entry_list.append(meta_data)
                    else:
                        filtered_entry_list.append(dir_entry)

            return filtered_entry_list

        return False

    @staticmethod
    def get_dir_metadata(dir_path, size_unit="k", time_format="%Y-%m-%d %I:%M:%S"):
        """
        Returns directory meta-data containing,
         - Last modified time
         - Directory size (sum of all file sizes)
         - Directory name
         - Directory parent directory
         - Directory full path

        :param dir_path: The full path of the directory to be analyzed.
        :param size_unit: Units in which to report directory size.
        :param time_format: Format in which to report directory modification time.

        :return: Dictionary containing relevant directory meta data.
        :rtype: dict
        """

        if DirUtils.check_valid_dir(dir_path):
            import datetime
            last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(dir_path)).strftime(time_format)

            # get file size in bytes
            file_size = os.path.getsize(dir_path)
            base_unit = 1024.0
            decimal_limit = 2

            if size_unit == "b":
                pass
            elif size_unit == "k":
                file_size /= base_unit
            elif size_unit == "m":
                file_size = (file_size / base_unit) / base_unit
            elif size_unit == "g":
                file_size = ((file_size / base_unit) / base_unit) / base_unit

            # limit floating-point value to X decimal points
            if size_unit != "b":
                file_size = round(file_size, decimal_limit)

            return {"LAST_MODIFIED": str(last_modified_time),
                    "SIZE": str(file_size),
                    "NAME": str(os.path.basename(dir_path)),
                    "PARENT_DIRECTORY": str(os.path.dirname(dir_path)),
                    "FULL_PATH": str(dir_path)}

        return False
