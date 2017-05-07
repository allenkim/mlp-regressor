from os.path import join


class FileManager(object):
    def __init__(self):
        self._data_dir = "data"
        self.managed_file = None

    def open_file(self, path):
        """
        Opens and returns the CSV file.
        :param path: File to read.
        :return: The opened file
        """
        file_path = join(self._data_dir, path)
        file = open(file_path, "r")
        self.managed_file = file
        return file

    def close_file(self):
        try:
            self.managed_file.close()
        except FileExistsError:
            print("File not found!")


class Yielder(object):
    def __init__(self):
        pass
    pass


if __name__ == "__main__":
    pass
