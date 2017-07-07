import setuptools
    

def read_file(file_path):
    with open(file_path, "r") as target_file:
        return target_file.read()

# retrieve information from package files
package_version = read_file("VERSION.txt")
package_requirements = read_file("requirements.txt").splitlines()
package_long_description = read_file("README.md")

config = {
    "name": "utilbox",
    "description": "Collection of utility packages for Python.",
    "long_description": package_long_description,
    "author": "Jenson Jose",
    "author_email": "jensonjose@live.in",
    "version": package_version,
    "install_requires": package_requirements,
    "packages": setuptools.find_packages(exclude=["tests"]),
    "classifiers": ["Development Status :: 3 - Alpha",
                    "Environment :: Console",
                    "Intended Audience :: Developers",
                    "License :: OSI Approved :: MIT License",
                    "Natural Language :: English",
                    "Operating System :: OS Independent",
                    "Programming Language :: Python :: 2.7",
                    "Topic :: Software Development",
                    "Topic :: Software Development :: Libraries :: Python Modules",
                    "Topic :: Utilities"]
}

setuptools.setup(**config)
