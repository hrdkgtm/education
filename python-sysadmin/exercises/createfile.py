#!/usr/bin/env python3
# Creating files based on user input

# Function to create a file
def get_file_name(reprompt=False):  # set a default parameter for reprompt
    if reprompt:                    # if reprompt is true, then the text will be printed
        print("Please enter a file name.")

    file_name = input("Destination file name: ").strip()    # a variable called file_name that is inputted by the user
    return file_name or get_file_name(True)                 # using the or, the function will return a variable called file_name or will re-run itself with reprompt=True

file_name = get_file_name()

print(f"Please enter your content. Entering an empty line will write the content to {file_name}:\n")

# open the file_name that is called from the function
with open(file_name, 'w') as f:     # put the file inside the 'f' object
    eof = False                     # set up an eof variable to stop the input if user enter nothing
    lines = []                      # set up a lines variable to store user input

    while not eof:                          # while not stopped
        line = input()                      
        if line.strip():                    # we are using the strip() so even if the user enter a whitespace, it will be false
            lines.append(f"{line}\n")       # append newlines
        else:
            eof = True                      # break the while loop if its end of line
        
    f.writelines(lines)                     # write everyline according to the 'lines' list
    print(f"Lines written {file_name}")     # notify