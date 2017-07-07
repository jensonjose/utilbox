def read_file(file_path):
    with open(file_path, "r") as target_file:
        return target_file.read()

# retrieve information from package files
package_version = read_file("VERSION.txt")

config_map = {
    "version": package_version,
    "author": "Jenson Jose",
    "settings": {
        "dependencies": {
            "required": True,
            "list": "requirements.txt"
        },
        "logging": {
            "message_format": "%(asctime)s : %(module)s (line %(lineno)d) : %(message)s",
            "timestamp_format": "%a %d %b %Y %H:%M:%S",
            "level": "debug",
            "write_mode": "a"
        }
    }
}
