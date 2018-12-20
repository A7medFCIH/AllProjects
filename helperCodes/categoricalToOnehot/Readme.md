# Categories To Onehot
- This script to help handling categorical Data columns.
- Contains Some functions :-
	- getEncoding
		- takes two pramaters realColumns, it's encoding
		- returns Dict(value : it's encode)
		- helps to keep track of modification for using in test Data.

	- categoriesToOnehot
		- takes two pramaters DF, columnName need to be converted.
		- return newDF, encoding(Dictionary), and newColumnsNames
	
	- encode
		- takes four pramaters DF, columnName, oldEncoding, and newColumnsNames
		- return newDF

- Happy using
- if there is any bugs, please take a screenshot of output, and inform me.