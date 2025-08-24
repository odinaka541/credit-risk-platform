# 541

""" let's make sense of the messy csv data, shall we"""

# ----- imports -----
import pandas as pd
import os
from pathlib import Path


# ----- ... -----
def analyze_dataset():
    """
    determine the architecture requirements for the DataManager class
    """

    dir_path = Path('data/raw')

    # does the file exist in the given directory?
    def discover_files(dir_path, filename: str):
        try:
            file_path = Path(dir_path) / filename # 'dir_path' is the directory
            return file_path.exists() and file_path.is_file()
        except (OSError, PermissionError) as e:
            print(f"There was an error finding the file in this directory: {e}")
            return False

    # it exists, how big is it?
    def analyze_file_sizes(file_path):
        try:
            return Path(file_path).stat().st_size
        except (FileNotFoundError, OSError, PermissionError) as e:
            print(f"There was an error analyzing the size of the file: {e}")
            return None

    # inspecting the data structure of the files
    def inspect_data_structure(file_path):
        try:
            df = pd.read_csv(file_path)
            return df.head(n = 5)
        except (FileNotFoundError, OSError, PermissionError) as e:
            print(f"There was an error analyzing the data structure: {e}")

    # what matters to us in the file (target variable):
    def identify_target_variable(file_path):
        try:
            df = pd.read_csv(file_path)

