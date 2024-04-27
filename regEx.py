import re

# Problem Statement:  Write a function that takes in a list of names,
# and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid,
# "Invalid name" if the name is not.

# Use the following list as an argument to test your function.

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def find_valid(name_list):
    for name in names:
        name_match = re.match(r"([A-Z][A-Za-z]+)(?: ([A-Z]\s?)?[A-Za-z-]+)+", name)
        if name_match:
            print(name)
        else:
            print("Invalid name. ")
    
    
print("Names: ")
find_valid(names)