# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:52:38 2020

@author: Julian Yates
Student #: 000758560
e-mail: julian.yates@mohawkcollege.ca

Create a command line interface for creating and comparing file hash values.  The script will accept a file path and using the hashlib library, generate a hash value for the file and save it to a hashes file or print it to standard out.  The script will also be able to generate a hash value for a file and compare it to the hash value saved in the hashes file.    Use hashlib.algorithms_available to determine the supported hashing algorithms. 

Test file path: "c:\\Users\\y8s\\strings.txt"
"""

import sys
import os


def texthash (usertext):
    '''
    Takes user defined input and creates a hash and outputs to stdout
    '''
    import hashlib
    blocks = 65536
    hashing = hashlib.sha512()
    with open(usertext, 'rb') as f:
          fileBytes = f.read(blocks)
          while len(fileBytes) > 0:
              hashing.update(fileBytes)
              fileBytes = f.read(blocks)
    return(hashing.hexdigest())

# intializes the choice variable
choice = 0
# intitializes the valid variable
valid = ''
# Asks the user to enter a file path
file = input("Enter a file path: ")
#checks the validity of the file path
if os.path.exists(file):
    # Enters a loop as long as choice equals less than 4
    while choice != "4":
        # Creates a variable with the user's input chosen from a menu 
        choice = input("What would you like to do with this hash? \n"
                       "\t 1. Print it to the screen.\n"
                       "\t 2. Store it in a file. \n"
                       "\t 3. Compare it to a previously saved hash. \n"
                       "\t 4. Quit\n"
                       "Type your choice here--->")
        # Validates the choice and ends the loop if a non int value is detected
        try:
            valid = int(choice)
        except ValueError:
            print("\nAw, you broke it! That is not a number!\n"
                  "Run it again and select a valid option. ")
            sys.exit(0)
        # Displays an error message and restarts the loop if the variable valid is greater than 4  
        if valid > 4:
            print("That is an invalid choice.Try again.")
        else:
            # uses the function texthash() to create a hash of the user defined file and print it to the screen 
            if valid == 1:
                print(texthash(file))  
            if valid == 2:
                # Hashes the user defined file
                newhash = texthash(file)
                # Asks for a file path to save the hash to
                hashfile = input("Enter a file to save the hash to: ")
                # Opens the file for appending
                appendfile = open(hashfile, 'a')
                # Appends the file with the file name and hash separated by a semi-colon
                appendfile.write( file + '; ' + newhash + "\n")
                # Closes the file
                appendfile.close()
            if valid == 3:
                # Asks for a user defined file containing the hash to compare
                hashfile = input("Enter the hash file containing the hash to compare: ")
                print ("Checking...\n")
                # Creates a hash of the user defined file
                newhash = texthash(file)
                # opens the file to a variable
                compareFile= open(hashfile)
                # extracts the filename from the path and appends a semi colon and a space
                fileName = file.rpartition('\\')[-1] + '; '
                # reads the lines in the file to match the stored hash to the new hash
                for line in compareFile:
                    # makes sure that there is an entry in the hash file for the filepath supplied by the user 
                    if line.split(";")[0] == file:
                        # Movesline into another variable
                        hashString = line
                        # Extracts the has from the line
                        theHash = hashString.partition(fileName)[2]
                        # Strips the trailing newline character from the hash
                        cleanHash = theHash.rstrip('\n')
                        # Compares the saved hash to the new hash and displays a message
                        if cleanHash == newhash:
                            print ("Hashes Match!")
                        else:
                            print("Hashes are different.")
                    # Prints a message if it cannot find the filepath, does not break the loop
                    else:
                        print ("Could not find a hash of " + file.rpartition('\\')[-1])
                # Closes the file containing the hash        
                compareFile.close()
# Prints an error message if the file path does not exist and exits the program
else:
    print("That file does not exist. Good-bye!")               