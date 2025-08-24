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

    data_path = Path('data/raw')

    # does the file exist in the given directory?
    def discover_files(data_path, filename: str):
        try:
            file_path = Path(data_path) / filename # 'data_path' is the directory
            return file_path.exists() and file_path.is_file()
        except (OSError, PermissionError):
            return False

    # it exists, how big is it?
    def analyze_file_sizes():
        pass
