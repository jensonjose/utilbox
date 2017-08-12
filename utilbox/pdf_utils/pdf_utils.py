"""
Utility module for handling PDF related operations.

Usage requires a working installation of the GhostScript application, available at:
https://www.ghostscript.com
"""

import subprocess

__author__ = "Jenson Jose"
__email__ = "jensonjose@live.in"
__status__ = "Alpha"


class PdfUtils:
    """
    Utility class containing methods for handling PDF related operations.
    """

    def __init__(self, gs_arch="x64"):
        self.gs_arch = gs_arch
        self.gs_command_map = {
            "x64": "gswin64",
            "x86": "gs"
        }
        self.gs_device_map = {
            "images": {
                "auto": {
                    "jpg": "jpeg"
                },
                "cmyk": {
                    "jpg": "jpegcmyk"
                },
                "grayscale": {
                    "jpg": "jpeggray"
                }
            }
        }

        self.gs_command = self.gs_command_map[self.gs_arch]

    def convert_to_images(self, source_path, destination_path, image_type="jpg", color_mode="auto", resolution="300"):
        """
        Converts a PDF file to a set of image files of specified file type.

        Number of generated image files is equal to the number of pages in the PDF file.

        :param source_path: The source file path of the PDF file to be converted.
        :param destination_path: The destination path of the target image file.
        :param image_type: The type of image file to be generated.
        :param color_mode: The colour mode of the target image file. Can be 'auto', 'cmyk' or 'grayscale'.
        :param resolution: The desired resolution of the target image, in ppi.

        :return: True if conversion was successful, False otherwise.
        :rtype: bool
        """

        from utilbox.os_utils import DirUtils
        from utilbox.os_utils import FileUtils

        if not FileUtils.check_valid_file(source_path):
            raise OSError("Error: Source path '%s' does not point to a valid file." % source_path)

        if not DirUtils.check_valid_dir(destination_path):
            # create the destination directory if it does not exist
            DirUtils.create_dir(destination_path)

        if color_mode in self.gs_device_map["images"]:
            if image_type in self.gs_device_map["images"][color_mode]:
                gs_device = self.gs_device_map["images"][color_mode][image_type]
                output_file_name_prefix = "pdf_page_"
                destination = str(destination_path) + "\\" + output_file_name_prefix + "%d.jpg"

                try:
                    args = self.gs_command +\
                           " -sDEVICE=" + gs_device +\
                           " -o" + destination +\
                           " -r" + resolution +\
                           " " + source_path

                    from utilbox.os_utils import SysUtils
                    SysUtils.start_process(args)
                except OSError:
                    raise OSError("Error: This utility requires a working installation of the GhostScript application "
                                  "(64-bit): '%s'. If you already have this installed, please check your PATH "
                                  "variable." % self.gs_command)
                except:
                    raise RuntimeError("Error: Unexpected error encountered while attempting to execute the GhostScript"
                                       " subprocess.")
            else:
                raise RuntimeError("Error: Unsupported image type was specified.")
        else:
            raise RuntimeError("Error: Unsupported color mode was specified.")
