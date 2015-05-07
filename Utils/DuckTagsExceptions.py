class DuckTagsRenameException(Exception):
    def __init__(self, error_path):
        self.error_path = error_path


class DuckTagsMultipleCoverDirectories(Exception):
    pass


class DuckTagsCorruptedMusicFile(Exception):
    pass