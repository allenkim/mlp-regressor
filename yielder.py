from os.path import join
import csv


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
        """
        Closes the file that was opened in the managed_file.
        :return: None
        """
        try:
            self.managed_file.close()
        except FileExistsError:
            print("File not found!")


class DataYielder(object):
    def __init__(self):
        pass

    @staticmethod
    def get_stock_data(csv_file):
        """
        :param csv_file: The csv file to read.
        :return: An array of closing price data.
        """
        for row in csv_file:
            if "symbol" in row:
                continue
            pass
