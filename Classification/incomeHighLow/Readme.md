# Income
- This model for predict if the income of the individual, will be greater than 50K or not.
Depending on some features (Age, Country, ...)
Detailed information about the dataset and all columns meaning in "adult.names" file.

- Using 2 layers of Deep NN.

- Working steps:-
	- Converting all categorical variables to onehot, asume missing values as new category, and generate one hot to represent it.
	- Standardize all quantitative variables.
	- Split The data to training set nd validation set.
	- Building the model.
	- Training the model.
	- Calculate the accuracy.

	- For more Information about every step fell free to ask me.

- Reached accuracy: 87%, Best previous model 86%, Check "adult.names" file for more information.

- Beginner Training points:-
Will not understand theis points until rebuild the model yourself.
	- modify stringToOnehot function :-
		- Make oneHot's columns --> 'ColumnCategory' insted of 'ColumnCategory.Code'
		- Return Dictionary {ColumnCategory : it's OneHot}
	- try to get Better accuracy.

