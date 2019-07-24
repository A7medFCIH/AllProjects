import numpy as np
import pandas as pd


def stockToDataset(stockColumn, stepSize):
    nObservation = stockColumn.shape[0]
    stockColumn = stockColumn.values
    observation = []
    response = []
    for i in range(stepSize, nObservation):
        observation.append(stockColumn[i - stepSize : i, :])
        response.append(stockColumn[i, :])
        pass

    observation = np.array(observation)
    response = np.array(response)
    if len(observation.shape) == 2:
        observation = observation[:, :, np.newaxis]
        pass
    return observation, response
