"""
Utility module to support manipulation of JSON data.
"""

import json

__author__ = "Jenson Jose"
__email__ = "jensonjose@live.in"
__status__ = "Alpha"


class JsonUtils:
    """
    Utility class containing methods for performing manipulation of JSON data.
    """

    def __init__(self):
        pass

    @staticmethod
    def convert_to_json(data_obj):
        """
        Converts supplied data object to JSON formatted string.

        :param data_obj: Data object to be converted to JSON.

        :return: The JSON formatted string.
        :rtype: str
        """

        return json.dumps(data_obj)
