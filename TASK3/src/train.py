import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def show_info(df):
    print(df.info())

def show_missing(df):
    print(df.isnull().sum())