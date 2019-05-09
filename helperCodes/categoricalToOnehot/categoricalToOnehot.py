import numpy as np
import pandas as pd

def getEncoding(realColumn, encodeedDF):
    '''
    Takes Data before, and after encoding, returns dictionary describe the mapping

    Parameters
    ----------
    realColumn : [any]
        contains the Data before encodeing

    encodeedDF : DataFrame
        contains the Data after encodeing
    
    Attributes
    ----------
    encodeing : dict
        store each category as key, and mapped encodeing as value

    stayUniques : [any]
        store the values we didn't find their encodeing yet
    
    Returns
    -------
    encodeing : dict
        store each category as key, and mapped encodeing as value
    '''
    _, encodeLength = encodeedDF.shape
    encoding = {}
    stayUniques = realColumn.unique().tolist()
    n = len(realColumn)
    for i in range(n):
        val = realColumn[i]
        if val in stayUniques:
            encode = encodeedDF.iloc[[i], :]
            encode = np.array(encode)[0].tolist()
            if encodeLength == 1:
                encode = encode[0]
            stayUniques.remove(val)
            encoding[val] = encode
        if stayUniques == []:
            break
    return encoding


def categoriesToOnehot(df, columnName):
    '''
    convert categorical values to onehot

    Parameters
    ----------
    df : DataFrame
        contains the data.

    columnName : str
        contains the name of column contains categorical data.
    
    Attributes
    ----------
    oneHotMatrix : np.matrix
        stores data in onehot format
    
    names : [str]
        contains new columns names
    
    encodeing : dict
        store each category as key, and mapped encodeing as value
    
    Returns
    -------
    df : DataFrame
        Data after encodeing
    
    encodeing : dict
        store each category as key, and mapped encodeing as value
    
    names : [str]
        contains new columns names
    '''
    oneHotMatrix = pd.get_dummies(df[columnName])
    
    names = []
    for categoryCode in oneHotMatrix:
        names.append(columnName + '_' + str(categoryCode))
    oneHotMatrix.columns = names
    
    encoding = getEncoding(df[columnName], oneHotMatrix)
    
    del df[columnName]
    df = df.join(oneHotMatrix)
    return df, encoding, names


def encode(df, columnName, encoding, newNames):
    '''
    maps data to desired encodeing, for testing, and predection using.

    Parameters
    ----------
    df : DataFrame
        Data before encodeing

    encodeing : dict
        contains encodeing rules as key value form

    newNames : [str] 
        contains new names for columns to be set
    '''
    dataEncoding = df[columnName].map(encoding)
    dataEncoding = pd.DataFrame(dataEncoding)
    if len(newNames) > 1:
        i = 0
        for newName in newNames:
            dataEncoding[newName] = dataEncoding[columnName].map(lambda x : x[i])
            i += 1
    del df[columnName]
    del dataEncoding[columnName]
    df = df.join(dataEncoding)
    return df

    

