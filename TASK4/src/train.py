import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def dataset_info(df):
    print(df.info())

def missing_values(df):
    print(df.isnull().sum())