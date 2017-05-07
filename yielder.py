from os.path import join


class FileManager(object):
    """
    Manages the files.
    """
    def __init__(self):
        self._data_dir = "data"
        self.managed_file = None

    def open_file(self, path):
        file_path = join(self._data_dir, path)
        file = open(file_path, "r")
        return file


class Yielder(object):
    def __init__(self):
        pass
    pass


if __name__ == "__main__":
    pass
