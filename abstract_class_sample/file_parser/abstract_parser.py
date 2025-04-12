from abc import ABC, abstractmethod

'''
Abstract Pattern Example
Imagine you’re designing a framework for reading and processing different types of files (e.g., CSV, JSON, XML). 
You can use an abstract base class to define a common interface for all file parsers while allowing each subclass 
to handle its specific file format.
'''
class FileParser(ABC):
    @abstractmethod
    def read_file(self, file_path):
        """Read and parse the file."""
        pass

    @abstractmethod
    def process_data(self):
        """Process the parsed data."""
        pass

    def parse_and_process(self, file_path):
        """Template method that combines file reading and processing."""
        data = self.read_file(file_path)
        return self.process_data()