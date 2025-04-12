import csv
import json
from file_parser.abstract_parser import FileParser

class CSVParser(FileParser):
    def read_file(self, file_path):
        print(f"Reading CSV file: {file_path}")
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            self.data = [row for row in reader]
        return self.data

    def process_data(self):
        print("Processing CSV data...")
        return {"row_count": len(self.data)}

class JSONParser(FileParser):
    def read_file(self, file_path):
        print(f"Reading JSON file: {file_path}")
        with open(file_path, mode='r') as file:
            self.data = json.load(file)
        return self.data

    def process_data(self):
        print("Processing JSON data...")
        return {"key_count": len(self.data.keys())}