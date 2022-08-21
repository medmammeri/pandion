import pandas as pd


def summerize(df: pd.DataFrame):
    return df.isnull().all().all()
