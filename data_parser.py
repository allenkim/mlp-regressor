import os
import csv
from datetime import datetime
from argparse import ArgumentParser

CSV_FILE = "prices.csv"
RAW_DATA_DIR = "unparsed_data"


def parse_data(path: str, company_symbol: [], target_file: str):
    root = os.path.dirname(os.path.realpath(__file__))
    for path, subdirs, files in os.walk(root):
        for name in files:
            file_path = os.path.join(path, name)
            if CSV_FILE in file_path:
                write_to_csv(file_path, company_symbol, target_file)


def write_to_csv(read_file: str, company_symbol: [], file_name: str):
    csv_to_read = csv.reader(open(read_file, newline=""))
    for row in csv_to_read:
        # Skip the first row in the csv file
        if "symbol" in row:
            with open(file_name, "a") as file:
                writer = csv.writer(file)
                writer.writerow(["SYMBOL", "CLOSING PRICE", "DAY", "DATE"])
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


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-s", "--symbol", type=str, help="The stock symbols to grab from the stock market.")
    arg_parser.add_argument("-r", "--read", type=str, help="CSV data to read")
    arg_parser.add_argument("-p", "--path", type=str, help="CSV file to generate")

    args = vars(arg_parser.parse_args())
    parse_data(args["read"], args["symbol"], args["path"])


if __name__ == "__main__":
    main()
