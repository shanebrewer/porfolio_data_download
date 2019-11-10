import pandas as pd
import time
import os
from pathlib import Path, PurePath
from datetime import datetime, timedelta


class data_importer:
    START_DATE = datetime(2017, 1, 1)
    END_DATE = datetime.now()
    BASE_DIRECTORY = PurePath('.')
    DATA_DIRECTORY = BASE_DIRECTORY.parent / 'data'
    INPUT_DATA_FILENAME = "TestData.csv"
    OUTPUT_DIRECTORY = BASE_DIRECTORY.parent / 'output'
    OUTPUT_EXCEL_FILENAME = "Market Data.xlsx"
    SLEEP_PERIOD = 0.1
    
    def __init__(self):
        pass


    def read_equity_list_from_csv(self, filename_and_path):
        print("Reading data file: " + filename_and_path)
        df = pd.read_csv(filename_and_path)
        return df
    