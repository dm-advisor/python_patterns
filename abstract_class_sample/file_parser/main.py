import sys
import pkg_resources


# This is the main module that imports and uses the CSVParser and JSONParser classes
from file_parser.abstract_subclass import CSVParser, JSONParser

def main():
    print("Now displaying sys.path=", sys.path) # Print the current Python path for debugging
    print('--------------')
    # Example usage of the CSVParser class
    csv_parser = CSVParser()
    csv_result = csv_parser.parse_and_process(pkg_resources.resource_filename("file_parser", "sample_data/example.csv"))
    print(csv_result)
    print('--------------')
    # Example usage of the JSONParser class
    json_parser = JSONParser() 
    json_result = json_parser.parse_and_process(pkg_resources.resource_filename("file_parser", "sample_data/example.json"))
    print(json_result)
    print('--------------')

if __name__ == "__main__":
    # Check if the script is being run directly
    main()