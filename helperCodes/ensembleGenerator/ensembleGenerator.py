
def ensembleCategoricalGenerator(generator, nBatches, batchSize):
    i = 0
    while i < nBatches:
        train_x, train_y = generator[i]
        yhat = classifier.predict(train_x)
        result = train_y[:, np.newaxis] == yhat.round()
        nCorrect = result.sum()
        correctWeight, incorrectWeight = .5/nCorrect, .5/(batchSize-nCorrect)
        weights = np.array([correctWeight if oneResult else incorrectWeight for oneResult in result])
        
        yield (train_x, train_y, weights)
        i = i + 1
        pass
    return
