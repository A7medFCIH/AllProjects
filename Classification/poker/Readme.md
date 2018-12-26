# Poker
- This model for classify what hand in poker player means.
Just takes the card rank and it's suit.
Detailed information about the dataset and all columns meaning in "poker.names" file.

- Using 24 layers of Deep NN.

- Working steps:-
	- Converting all categorical variables to onehot, asume missing values as new category, and generate one hot to represent it.
	- Standardize all quantitative variables.
	- Split The data to training set nd validation set.
	- Building the model.
	- Training the model.
	- Decay the learning rate.
	- Calculate the accuracy.

	- For more Information about every step fell free to ask me.

- Reached accuracy: 98.25%.

- Beginner Training points:-
	- Find Good learning rate decay to reach 100% accuracy.

