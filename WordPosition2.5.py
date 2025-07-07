# Program should calculate position of a specific string in a file 
# The positon should be expressed as a percent. # For example, “the word was found at the point 10.4% of the way through the file.” 

# percentage = (wordposition / ken file_contents) * 100

# 10. The output message printed to the terminal should be modified, so that it only says which quarter
# of the file the target string occurred in. For example: “The string <STRING> was found in the
# <first/second/third/fourth> quarter of the file <FILEPATH>.”

# 11. The file output should still include the exact percentage of the position. 
# (This is not exactly a “new” Feature. This just clarifies that Feature 7 should still include the exact percentage,
# not just the “quarter”.

# Program should help user by first printing out the current working directory, and a list of the contents of that directory,
# to help user enter in a proper path to a file
# use os from #6 to print out current working directory, and a list of contents of directory, to help user enter in a proper path to a file
import os

os.getcwd()  #getcwd = get current working directory
os.listdir()
os.path.isfile("wordposition_results.txt")  #True      #using very basic boolean functions to help me remember how it works
os.path.isdir("wordposition_results.txt")   # False     
os.path.isdir("monty_python_sketches")      # True
os.path.exists("wordposition_results.txt")  # True

# TODO program asks user to specify path to the file to be searched
# TODO Then have data read from the file
# TODO if user enters wrong path, give user helpful message & new chance to provide valid path 
# #try except solves this

try:
    file_path = input("Specify path to a file to be searched: ")   
    with open(file_path, "r") as f:
        file = f.read()
        print(file)        
except FileNotFoundError:
    print("Wrong path, you entered wrong file path!")
    try:
        file_path = input("Specify path to a file to be searched again: ")  
        with open(file_path, "r") as f:
            file = f.read()
            print(file)  
    except FileNotFoundError:
        print("Wrong file again dummy, ending program.")



###############

# TODO program ask the user to specify the word to be located
specified_word = input("specify word to be located: ")
file_length = len(file)
word_found = file.find(specified_word)


# TODO calculate position of specific string in a file   #done 
# ???   # len(sample_string) ??     # sample_string.find() ?? 

# specified_word = input

word_percentage = (word_found / file_length) * 100


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

# watch f string video to learn how to finish and other tutorials



# TODO include exact percentage of position for the file output - #11 - done above line



 # print("The string" + <STRING> "was found in the", <first/second/third/fourth>, "quarter of the file", <FILEPATH>, sep = "\n")



# TODO print out results message to file called "wordposition_results.txt"
# print the percentage. But where do I put the percentage?
# print("The string <STRING> was found in the <first/second/third/fourth> quarter of the file <FILEPATH>")
