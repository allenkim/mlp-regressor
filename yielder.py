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
    @staticmethod
    def get_stock_data(csv_file):
        """
        :param csv_file: The csv file to read.
        :return: An array of data non repeated.
        """
        # Stock data should contain the a tuple of day numbers and its
        stock_data = []
        for row in csv_file:
            if "symbol" in row:
                continue
            else:
                split_row = row.split(",")
                stock_data.append(split_row[1])
        return stock_data

    @staticmethod
    def get_structured_data(data):
        # A matrix of structured data
        structured_data = []
        for row in range(0, len(data)):
            # Create a new array
            sub_data = []
            current_row = data[row]
            sub_data.append(current_row)
            for index in range(1, 5):
                try:
                    sub_data.append(data[index + row])
                except IndexError:
                    # Reaching the end of the array
                    # structured_data.append(sub_data)
                    continue
            if len(sub_data) < 5:
                continue
            structured_data.append(sub_data)
        return structured_data
