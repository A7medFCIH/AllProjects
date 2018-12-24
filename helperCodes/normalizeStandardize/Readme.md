# Data Slicing
This script is to help in spliting the data

normalize:-
    - This function normalizr the columns values to range 0:1
    - Takes: DataFrame(Dataset), list(columnsNames)
    - returns Normalized df

standardize:-
    - This function standardize the columns values to standard normal distruibution
    - Takes: DataFrame(Dataset), list(columnsNames)
    - returns standardized df

adaptNormalize:-
    - This function normalizr the columns values to range 0:1, depending on preivous values of minimun, maximum
    - Takes: DataFrame(Dataset), list(columnsNames, minimun, maximum)
    - returns Normalized df

adaptStandardize:-
    - This function standardize the columns values to standard normal distruibution,depending on preivous values mean, std
    - Takes: DataFrame(Dataset), list(columnsNames, mean, maximstdum)
    - returns standardized df

