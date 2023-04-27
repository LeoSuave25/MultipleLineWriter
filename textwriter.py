# Style the Entire Program
# Make a function to write to a file
def writer(to_write):
    with open('myfile.txt', 'a') as outputfile:
        outputfile.write(str(to_write) + "\n")
# Ask for user input what to write in the myfile.txt
print("Enter line")
words_to_write = input()
writer(words_to_write)
# Put it in a while loop with a condition if response is 'y'