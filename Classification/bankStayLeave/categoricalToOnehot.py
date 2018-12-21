import numpy as np
import pandas as pd

def getEncoding(realColumn, encodeedDF):
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

    

