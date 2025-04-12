from setuptools import setup, find_packages

setup(
    name="file_parser",  # Package name
    version="0.1",       # Version number
    description="A Python package for parsing and processing files",  # Short description
    author="Hooman",     # Author's name
    packages=find_packages(),  # Automatically find all subpackages
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    package_data={
        'file_parser': ['sample_data/example.csv','sample_data/example.json'],  # Explicitly declare files to include
    },

    # install_requires=[
    #     "pandas>=1.0.0",       # Example dependency for handling tabular data
    #     "openpyxl>=3.0.0"      # Example dependency for Excel file support
    # ], # Uncomment and add dependencies as needed
    # TODO: Figure out why run-file-parser throws an error: ModuleNotFoundError: No module named 'abstract_class_sample'
    entry_points={
        "console_scripts": [
            "run-file-parser=file_parser.main:main",  # Command-line shortcut to run main.py
        ],
    },
    python_requires=">=3.6",  # Minimum Python version required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)