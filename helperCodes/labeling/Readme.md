# Label Data
- This is script to help in hand data labeling.

- Put all data files if dir(Data), and run the script, and start labeling.

- Working steps:-
	- Fill colum's list with all your columns names, don't forget observation column
	- script read all files in dir(Data), and go one by one
		- if the file prelabeled, the script path it
		- if not, iter in each observation and asks to put response, put them as numbers EX:"111" for 3 true classes
		- then the script made a file with same name in dir(labelData)

	- For more Information about every step fell free to ask me.

- Beginner Training points:-
	- Add ability to continue file
	- Add ability to stop in any time
	- Add ability to go back for previous observation
