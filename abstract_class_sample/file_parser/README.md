# File Parser

A sample Python package for parsing and processing different file formats like CSV, JSON, and more.
This package is implemented by using an abstract base class and two subclasses (one for CSV and another for JSON).

The `file_parser` package provides a flexible and extensible framework for file handling, allowing developers to implement custom file processing workflows with ease. You can create additional subclasses for other file types (e.g., XML).

---

## Features

- Support for multiple file formats (e.g., CSV, JSON).
- Easy-to-use base class for creating custom parsers.
- Built-in logging for process tracking and debugging.
- Extendable and modular structure for scalability.

---

## Installation

1. Clone the repository or download the source files.
2. Navigate to the package parent directory.
3. Install the package and dependencies:

```bash
   git clone https://github.com/dm-advisor/python_patterns.git
   cd ~/python_patterns/abstract_class_sample
   pip install .
```

---

## Execution

To run the main() function in the package type the following command in a terminal:

```bash
   cd ~/python_patterns/abstract_class_sample
   run-file-parser
```

---

## Usage

Example: Parsing CSV Files

```python
from file_parser.csv_parser import CSVParser

# Initialize the parser
csv_parser = CSVParser()

# Parse and process a CSV file
result = csv_parser.parse_and_process("Your CSV file path and name")
print(result)  # Output: {'row_count': <number_of_rows>}
```

---

## Package File Structure

```plaintext
file_parser/
├── __init__.py          # Package initialization
├── abstract_parser.py   # Base abstract class for file parsers
├── abstract_subclass.py # CSV and Json parsers implementation
├── sample_data/         # Example input files
│   ├── example.csv
│   └── example.json
└── main.py              # Sample script demonstrating usage
```

---

## Dependencies

The following Python libraries are required:
None
If any dependencies, install them using:

```bash
   pip install -r requirements.txt
```

---

## Package Build

To build the package enter the following commands in a terminal:

```bash
   cd ~/python_patterns/abstract_class_sample
   python setup.py sdist
   pip install dist/file_parser-x.x.tar.gz
```
Note 1: In the above pip command, replace x.x with the correct package version as specified in the setup.py file.

Note 2: To see information about the installed package use: ``` pip show file_parser ```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
