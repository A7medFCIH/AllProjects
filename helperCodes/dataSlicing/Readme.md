# Data Slicing
This script is to help in spliting the data
Has Two functions.

spiltData:-
    - This Function split the Data to -> Train, Validation, and Test
    - Depending on Test Percentage
    - Takes: DataFrame(Dataset), float(Percentage), bool(needValidation)
    - returns list, each element in it is a tuple has (Data, Label)

batching:-
    - This Funcing split Training Data To many Batches
    - Depending on Batch size
    - takes: DataFrame(trainData), DataFrame(trainLabel), int(size)
    - returns : Dict{}, each element in it is a tuple has (Data, Label)


