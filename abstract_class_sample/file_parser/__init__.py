# __init__.py
import logging
# __init__.pyfrom .abstract_parser import FileParser
from file_parser.abstract_subclass import CSVParser, JSONParser

# Configure logging for the package
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

__all__ = ["CSVParser", "JSONParser"]  # Optional: restrict what's accessible