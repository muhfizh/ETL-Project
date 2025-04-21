import pandas as pd

def extract_excel(file_path):
    df = pd.read_excel(file_path)
    print('extract Success')
    return df

def extract_csv(file_path):
    df = pd.read_csv(file_path)
    print('extract Success')
    return df