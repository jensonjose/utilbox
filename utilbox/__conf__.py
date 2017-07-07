config_map = {
    "version": "0.1.3",
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
