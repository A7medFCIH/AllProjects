import numpy as np
import pandas as pd

def normalize(df, columns):
    '''
    normalize quantitative variable to [0-1] range

    Paremeters
    ----------
    df : DataFrame
        The hole data set
    
    columns : [str]
        names of quantitative columns
    
    Attributes
    ----------
    minimun : [float]
        minmum value in each column
    
    maximum : [float]
        maximum value in each column
    
    Returns
    -------
    df : DataFrame
        Data after normalization
    '''
    minimun = df[columns].min()
    maximum = df[columns].max()
    df[columns] = (df[columns] - minimun) / (maximum - minimun)
    return df, minimun, maximum


def standardize(df, columns):
    '''
    standardize quantitative variable to mean 0, std 1

    Paremeters
    ----------
    df : DataFrame
        The hole data set
    
    columns : [str]
        names of quantitative columns
    
    Attributes
    ----------
    mean : [float]
        mean value in each column
    
    std : [float]
        std value in each column
    
    Returns
    -------
    df : DataFrame
        Data after standardize
    '''
    mean = df[columns].mean()
    std = df[columns].std()
    df[columns] = (df[columns] - mean) / std
    return df, mean, std


def adaptNormalize(df, columns, minimun, maximum):
    '''
    to adapt normalization in validation,testing, and prediction time

    Paremeters
    ----------
    df : DataFrame
        The hole validation, or testing data
    
    minimun : [float]
        the minimun value in each column from training set
    
    maximum : [float]
        the maximum value in each column from training set
    
    Returns
    -------
    df : DataFrame
        Data after normalization
    '''
    df[columns] = (df[columns] - minimun) / (maximum - minimun)
    return df


def adaptStandardize(df, columns, mean, std):
    '''
    to adapt standardize in validation,testing, and prediction time

    Paremeters
    ----------
    df : DataFrame
        The hole validation, or testing data
    
    mean : [float]
        the mean value in each column from training set
    
    std : [float]
        the std value in each column from training set
    
    Returns
    -------
    df : DataFrame
        Data after standardize
    '''
    df[columns] = (df[columns] - mean) / std
    return df

# normalize Image by (image / 255.) --> so the values become 0:1
    
