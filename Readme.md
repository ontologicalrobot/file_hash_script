This script takes a user input file path and send it to a function which creates a SHA512 encoded hash of the file.

The script then enters a loop which presents 4 options to the user:
	1 print the hash to stdout
	2 save the hash to a file 
	3 compare the hash to a previously saved hash
	4 quit

There is some error checking which prevents incorrect filepath errors, and incorrect option input.