from setuptools import setup, find_packages

setup(
    name="file_parser",                           # Package name
    version="1.0",                                # Version number
    description="A Python package for parsing and processing files",  # Short description
    author="dm-advisor",                          # Author's name
    author_email="datamunge.advisor@gmail.com",   # Author's email
    url="https://github.com/hooman/file_parser",  # "Home-page"
    packages=find_packages(),                     # Automatically find all subpackages
    include_package_data=True,                    # Include additional files specified in MANIFEST.in
    package_data={
        'file_parser': ['sample_data/example.csv','sample_data/example.json'],  # Explicitly declare files to include
    },

    # install_requires=[
    #     "pandas>=1.0.0",       # Example dependency for handling tabular data
    #     "openpyxl>=3.0.0"      # Example dependency for Excel file support
    # ], # Uncomment and add dependencies as needed

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
    license="MIT",  # License type
    # long_description=open("README.md").read(),  # Long description from README file
    # long_description_content_type="text/markdown",  # Format of the long description
    keywords="file parsing, data processing, file handling",  # Keywords for the package
    platforms="any"  # Supported platforms
)