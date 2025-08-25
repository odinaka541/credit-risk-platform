# 541

""" let's make sense of the messy csv data, shall we"""

# ----- imports -----
import pandas as pd
import os
from pathlib import Path


# ----- ... -----


class DataAnalyzer:

    def analyze_dataset(self):
        """
        determine the architecture requirements for the DataManager class
        """

        dir_path = Path('data/raw')

        # does the file exist in the given directory?
        def discover_files(dir_path, filename: str):
            try:
                file_path = Path(dir_path) / filename # 'dir_path' is the directory
                return file_path.exists() and file_path.is_file()
            except Exception as e:
                print(f"There was an error finding the file in this directory: {e}")
                return False

        # it exists, how big is it?
        def analyze_file_sizes(file_path):
            try:
                return Path(file_path).stat().st_size
            except Exception as e:
                print(f"There was an error analyzing the size of the file: {e}")
                return None

        # inspecting the data structure of the files
        def inspect_data_structure(file_path):
            try:
                df = pd.read_csv(file_path)
                return df.head(n = 5)
            except Exception as e:
                print(f"There was an error analyzing the data structure: {e}")

        # identifying the target variable:
        def identify_target_variable(file_path):
            try:
                df = pd.read_csv(file_path)
                target_variable = df["loan_status"]
                return target_variable
            except Exception as e:
                print(f"There was an error identifying the target variable: {e}")
                return None

        # what are the memory requirements for the files:
        def assess_memory_requirements(file_path):
            try:
                file_size_bytes = Path(file_path).stat().st_size
                estimated_memory = file_size_bytes * 3 # csv files use 2-4x file size
                return estimated_memory
            except Exception as e:
                print(f"There was an error identifying the size of the file: {e}")
                return None


# ----- ... -----
if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.analyze_dataset()
