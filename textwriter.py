# Style the Entire Program
# Make a function to write to a file
def writer(to_write):
    with open('myfile.txt', 'a') as outputfile:
        outputfile.write(str(to_write) + "\n")
# Ask for user input what to write in the myfile.txt
# Put it in a while loop with a condition if response is 'y'
response = 'y'
while response.lower() == 'y':
    print("Enter line")
    words_to_write = input()
    writer(words_to_write)
    while True:
        print("Are there more lines? (y/n)")
        response = input()
        if response.lower() in ('y', 'n'):
            break
        else:
            print("Invalid Response. Please Enter y or n ")
        