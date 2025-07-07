# EDITED ON 4/4/25, improving on code since admission. This is a copy of wordposition 3, but adding more details in this file for now.

# Program should calculate position of a specific string in a file 
# The positon should be expressed as a percent. # For example, “the word was found at the point 10.4% of the way through the file.” 

# percentage = (wordposition / ken file_contents) * 100

# 10. The output message printed to the terminal should be modified, so that it only says which quarter
# of the file the target string occurred in. For example: “The string <STRING> was found in the
# <first/second/third/fourth> quarter of the file <FILEPATH>.”

# 11. The file output should still include the exact percentage of the position. 

#################

# New features of Word Position 3.0
# In versions 1.0 and 2.0, the user would have to re-run the program every time they wanted to search
# for a particular word in a particular file. In this version, the capabilities will be expanded to include
# repeated searching. In order to satisfy the client, you need to complete Feature 15 OR Feature 16.
#Completing both is also allowed, but not required at this time.

#15. Instead of searching in a single file, the program should ask the user for a directory path (not
# a single file path), and results should be provided for every file in that directory. 
# This includes both the printed results and the results written to the output file.

# 17. In Feature 9 of WP 2.0, the user was given one additional attempt to enter a correct file path. In
# this version, the program should continue asking for a valid path until either a) the user provides
# a valid path, or b) the user opts to quit the program. (Tip: this means providing a valid directory
# path if you are implementing Feature 15, or a valid file path otherwise.)   *** *** ***


# Dictionaries (see Pattern 7.3) excel at containing structured data, so that you can easily access
# values later, kind of like looking them up in a reference table. Think about the multiple pieces
# of data that you are tracking with each loop/run in the program, and think about how that data
# could be captured all together in a dictionary.

# • Tuples (see Pattern 7.4) are a little less intuitive, since they are essentially just immutable lists.
# Think about if there’s something in your data that could be represented as a pair of values or
# a triple of values instead of just a single value or an arbitrary list of values. This might be a
# good candidate for a tuple. At this stage, you are encouraged to just try something; you will
# not be penalized for “doing it wrong”, but it may help you realize how to “do it right” in later
# assignments.3
####################
    # NEW PATTERNS #TODO
# PATT 6.1 used a “switch”-type while-loop to loop until a condition happens    # done
# PATT 6.2 used for-loop over an iterable like a list, tuple, or dictionary
# PATT 6.3 updated results inside a loop (e.g., incremented/updated/appended)

# PATT 7.1 used a list where a list is appropriate & useful
# PATT 7.2 used indexing (by index or key) with a list, tuple, or dictionary
# PATT 7.3 used a dictionary for an appropriate data structure
# PATT 7.4 used a tuple where appropriate (unpacking and/or immutable data)

#######################

# Finally, note that there are Patterns related to dictionaries (Pattern 7.3) and tuples (Pattern 7.4), 
# but it would be technically possible to implement the new Features without including these Patterns. 
# So if you want to be able to score those Patterns,
# you will need to think about ways that these structures might be helpful or appropriate in your code.  *********************

# TODO: Figure out how dictionaries and tuples might be helpful or appropriate in my code

#######################################################################################

# 17. In Feature 9 of WP 2.0, the user was given one additional attempt to enter a correct file path.
# In this version, the program should continue asking for a valid path until either
#  a) the user provides a valid path, or b) the user opts to quit the program. 
# (Tip: this means providing a valid directory path if you are implementing Feature 15, or a valid file path otherwise.)   *** *** ***
# Will be doing Feature 15 and Feature 17 a       ***

# Program should help user by first printing out the current working directory, and a list of the contents of that directory,
# to help user enter in a proper path to a file
# use os from #6 to print out current working directory, and a list of contents of directory,
# to help user enter in a proper path to a directory path and then to a file

import os

os.getcwd()  #getcwd = get current working directory
os.listdir()
#directory_path = os.listdir()      ## do I use this with "while" loop or no? need to figure that out.
#print(directory_path)
# os.path.isfile("wordposition_results.txt")  #True      #using very basic boolean functions to help me remember how it works
# os.path.isdir("wordposition_results.txt")   # False  
# os.path.isdir("monty_python_sketches")      # True
# os.path.exists("wordposition_results.txt")  # True

# TODO program asks user to specify path to a directory path to be searched, and results should be provided for every file in that directory. 
# This includes both the printed results and the results written to the output file.
# TODO Then have data read from the file
# TODO if user enters wrong path, give user helpful message & new chance to provide valid directory path,
# continue asking for valid path until given one by user.

# Maybe look at lists2 to help solve and use for providing inputed directory path.
# Need to use a "switch"-type While-loop until a condition happens with try except
# I'm starting to better understand how to use the "while loop." But still need to better understand how to use for-loops.
# I also can't figure out where to put lists, tupiles, and dictionaries. Need to improve on that and better understand how & where to use them 

# TODO Use a switch loop with try except. Use while before try except
# TODO program should continue asking for a valid path until either 
    # a) the user provides a valid path, or b) the user opts to quit the program. 
    # (Tip: this means providing a valid directory path with implementing feature 15. ******* **********

# I have to rewatch the tutorials to learn how to implement def functions
# def get_valid_path(is_directory=False):                           
# reimangine a chunk
# figure out return - output
# argument - input
# probably copy and paste into body of function, revise to fit  # reimagine using code over again.
# test it out to make sure it works. # once tsted, put function instead of loop
# wont have to modify hardly any pre-existing code
while True:
    path = input("Specify a directory path to be searched: \n")
    if os.path.isdir(path):
        file_name = input("Specify a file name inside the directory: ")     # could use list dir # think about for loop
        file_path = path + "/" + file_name  
        break  
    elif os.path.isfile(path):
        file_path = path
        break
    else:
        print("invalid path. Enter again or quit")

with open(file_path, "r") as fc:        #fc = file connection
    file_contents = fc.read()
    print(file_contents)  
    
# TODO now ask user for file path to be searched and then ask for word to be searched within file
try:   
    file_path = input("Specify path to a file path to be searched: ")   
    with open(file_path, "r") as f:
        file = f.read()
        print(file)        
except FileNotFoundError:
    print("Wrong path, you entered wrong file path!")
    try:
        file_path = input("One more try. Specify path to a file path to be searched again: ")  
        with open(file_path, "r") as f:
           file = f.read()
           print(file)  
    except FileNotFoundError:
        print("Ok, ending program.")    
    
###############


# TODO program ask the user to specify the word to be located  ##From line 139 there's an error  ****  ***  ***
specified_word = input("specify word to be located: ")
file_length = len(file_contents)             # from line 139 - end of code    # possiblly change word to be specifiedGre
word_found = file_contents.find(specified_word)

# word_found = the word found in the file
# file_length = the length of characters in the file


# TODO calculate position of specific string in a file   #done 
# ???   # len(sample_string) ??     # sample_string.find() ?? 

# specified_word = input
# word_percentage is percentage of the word found in file


word_percentage = (word_found / file_length) * 100  # this is calculation


if word_percentage <= 25.00:
    quarter = " the 1st quarter of "
elif word_percentage >= 25.01 and word_percentage <= 50.00:
    quarter = " the 2nd quarter of "    
elif word_percentage >= 50.01 and word_percentage <= 75.00:
    quarter = " the 3rd quarter of "
else:
    quarter = " the 4th quarter of "

 #print("position of word is + <STRING> "was found in the", quarter, <FILEPATH>, sep = "\n")
 # TODO the output message printed to the terminal should be modified, so that it only says which quarter
    # of the file the target string occurred in. For example: “The string <STRING> was found in the
    # <first/second/third/fourth> quarter of the file <FILEPATH>.
print("position of word is: ", quarter, file_path, sep = "\n")


# TODO include exact percentage of position for the file output - #11 - done above line
 # print("The string" + <STRING> "was found in the", <first/second/third/fourth>, "quarter of the file", <FILEPATH>, sep = "\n")

# TODO print out results message to file called "wordposition_results.txt"
# Need to figure out why the text file won't properly open and resolve it - possibly have solved it, check after fixing code above
# with open("inserttextfilehere.txt", mode = "w") as write_connection
# write_connection.write("position of word is: ",quarter, file_path, sep = "\n")
#quarter = 1
#file_path = 3

with open("wordposition_results.txt", mode = "a") as file_connection:
    file_connection.write(f"position of word is: {quarter}, {file_path}")
    #print("position of word is: ", quarter, file = file, sep = "\n")
