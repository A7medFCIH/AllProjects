import numpy as np
import pandas as pd

def normalize(df, columns):
    minimun = df[columns].min()
    maximum = df[columns].max()
    df[columns] = (df[columns] - minimun) / (maximum - minimun)
    return df


def standardize(df, columns):
    mean = df[columns].mean()
    std = df[columns].std()
    df[columns] = (df[columns] - mean) / std
    return df
