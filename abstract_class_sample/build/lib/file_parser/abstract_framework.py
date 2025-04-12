import pkg_resources

from file_parser.abstract_subclass import CSVParser
from file_parser.abstract_subclass import JSONParser

# Create parser instances
csv_parser = CSVParser()
json_parser = JSONParser()

# Parse and process a CSV file
csv_result = csv_parser.parse_and_process(pkg_resources.resource_filename("file_parser", "sample_data/example.csv"))
print(csv_result)  # Output: {'row_count': X}

# Parse and process a JSON file
json_result = json_parser.parse_and_process(pkg_resources.resource_filename("file_parser", "sample_data/example.json"))
print(json_result)  # Output: {'key_count': Y}