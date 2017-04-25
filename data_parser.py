import os
import csv
import sys
from datetime import datetime

CSV_FILE = "prices.csv"
RAW_DATA_DIR = "unparsed_data"


def parse_data(path: str, company_symbol: [], target_file: str):
    root = os.path.dirname(os.path.realpath(__file__))
    print(root)
    for path, subdirs, files in os.walk(root):
            for name in files:
                file_path = os.path.join(path, name)
                if CSV_FILE in file_path:
                    # print(file_path)
                    write_to_csv(file_path, company_symbol, target_file)


def write_to_csv(read_file: str, company_symbol: [], file_name: str):
    csv_to_read = csv.reader(open(read_file, newline=""))
    for row in csv_to_read:
        # Skip the first row in the csv file
        if "symbol" in row:
            continue

        if company_symbol[0] in row[0] or company_symbol[1] in row[0]:
            current_date = row[1] # Get the current day
            split_date = current_date.split("-") # Split the date into an array of years, month, days
            # Create the datetime object
            current_datetime = datetime(year=int(split_date[0]), month=int(split_date[1]), day=int(split_date[2]))
            # Determine the type of day
            weekday = current_datetime.weekday()
            closing_price = row[5] # Get the closing price

            with open(file_name, "a") as file:
                fields = [company_symbol, closing_price, weekday, current_date]
                writer = csv.writer(file)
                writer.writerow(fields)


if __name__ == "__main__":
    parse_data(RAW_DATA_DIR, ("TMUS", "TMUSP"), "t_mobile_2016.csv")
