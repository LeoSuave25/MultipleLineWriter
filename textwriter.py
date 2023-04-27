# Style the Entire Program
import pyfiglet as fig
print("\033[32m","="*100,"\033[m")
title = "Multiple Line Writer"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M Suaverdez",font="bubble"))
# Make a function to write to a file
def writer(to_write):
    with open('myfile.txt', 'a') as outputfile:
        outputfile.write(str(to_write) + "\n")
# Ask for user input what to write in the myfile.txt
# Put it in a while loop with a condition if response is 'y'
response = 'y'
while response.lower() == 'y':
    print("\033[1;32mAre there more lines? (y/n)\033[0m")
    words_to_write = input()
    writer(words_to_write)
    while True:
        print("\033[1;32mAre there more lines? (y/n)\033[0m")
        response = input()
        if response.lower() in ('y', 'n'):
            break
        else:
            print("\033[1;31mInvalid Response. Please Enter y or n.\033[0m")

print("\033[32m","="*100,"\033[m")