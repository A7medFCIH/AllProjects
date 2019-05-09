def spiltData(dataset, testPercentage, validation=0):
    '''
    Helps in dividing data into train, validation, and test sets

    Parameters
    ----------
    dataset : DataFrame
        The hole data set
    
    testPercentage : float
        The percentage we take for validation or test sets
    
    validation : boolean
        indicates for needing validation set or not
    
    Attributes
    ----------
    testSize : int
        the size of test or validation set
    
    .*Data : DataFrame
        The observation
    
    .*label : pd.Series
        The response
    
    Returns
    -------
    _ : [()]
        list of tuble each element in list contains observation, and response
    '''
    testSize = int(dataset.shape[0] * testPercentage)
    testSize = min(testSize, 10**4)
    testSize = max(testSize, 2000)
    totalSize = testSize + (testSize * validation)
    
    trainData = dataset.iloc[:-totalSize, :-1]
    trainLabel = dataset.iloc[:-totalSize,-1:]
    
    testData = dataset.iloc[-testSize: , :-1]
    testLabel = dataset.iloc[-testSize:, -1:]
    if validation == 1:
        validationData = dataset.iloc[-totalSize:-testSize, :-1]
        validationLabel = dataset.iloc[-totalSize:-testSize, -1:]
        
        return (trainData, trainLabel), (validationData, validationLabel), (testData, testLabel)
    return (trainData, trainLabel), (testData, testLabel)


def batching(trainData, trainLabel, batchSize):
    '''
    Helps in dividing data into batches

    Parameters
    ----------
    trainData : DataFrame
        training set observation
    
    trainLabel : DataFrame
        training set response
    
    batchSize : int
        number of samples in each batch
    
    Attributes
    ----------
    batches : {}
        contains key(number of batch) -> value (tuble(batchObservation, batchResponse))
    '''
    batches = {}
    nCompletebatch = int(trainData.shape[0] / batchSize)
    restFromBatches = trainData.shape[0] % batchSize
    
    for i in range(nCompletebatch):
        start = i * batchSize
        end = start + batchSize
        trainDataBatch = trainData.iloc[start:end, :]
        rainLabelBatch = trainLabel.iloc[start:end, :]
        batches[i] = (trainDataBatch, rainLabelBatch)
    trainDataRest = trainData.iloc[-restFromBatches:, :]
    trainLabelRest = trainLabel.iloc[-restFromBatches:, :]  
    batches[nCompletebatch] = (trainDataRest, trainLabelRest)
    
    return batches
    