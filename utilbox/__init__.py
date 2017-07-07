import os
import sys
import json

# CHECK DEPENDENCIES

# check python version
if sys.version_info < (2, 7):
    raise RuntimeError("Fatal error: Python 2.7+ is required for this package.")

# RETRIEVE PACKAGE INFORMATION FROM CONFIG FILE

try:
    import __conf__
    config = __conf__.config_map
except ImportError:
    raise RuntimeError("Fatal error: Configuration module is missing.")

__author__ = config["author"]
__version__ = config["version"]
__version_info__ = tuple([int(d) for d in __version__.split(".")])

# CHECK FOR PACKAGE DEPENDENCIES

if "dependencies" in config:
    if "required" in config["dependencies"]:
        if config["dependencies"]["required"]:
            dependency_list = []
            if "list" in config["dependencies"]:
                with open(config["dependencies"]["list"], 'rU') as dependencies:
                    for dependency in dependencies:
                        dependency_list.append(dependency)

                import pkg_resources
                if len(dependency_list) > 0:
                    try:
                        pkg_resources.working_set.require(dependency_list)
                    except Exception as ex:
                        print "A required application dependency is missing."

# DEFINE '*' IMPORTABLE CLASSES IN THIS PACKAGE

# not needed as all packages are required
