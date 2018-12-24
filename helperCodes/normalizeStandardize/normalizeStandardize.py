import numpy as np
import pandas as pd

def normalize(df, columns):
    minimun = df[columns].min()
    maximum = df[columns].max()
    df[columns] = (df[columns] - minimun) / (maximum - minimun)
    return df, minimun, maximum


def standardize(df, columns):
    mean = df[columns].mean()
    std = df[columns].std()
    df[columns] = (df[columns] - mean) / std
    return df, mean, std


def adaptNormalize(df, columns, minimun, maximum):
    df[columns] = (df[columns] - minimun) / (maximum - minimun)
    return df


def adaptStandardize(df, columns, mean, std):
    df[columns] = (df[columns] - mean) / std
    return df

# normalize Image by (image / 255.) --> so the values become 0:1
    
