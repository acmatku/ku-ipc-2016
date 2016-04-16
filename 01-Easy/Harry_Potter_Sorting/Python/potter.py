'''
ACM@KU Intramural Programming Competition 2016

Author: Stefan Mendoza
Problem: Harry Potter Sorting
'''

import sys

# Open the file & read it, removing any whitespace at the end of the file
f = open(sys.argv[1])
file_text = f.read().strip().split('\n')

'''
-   Grab the number of students from the first line in the file
-   Make a tuple list of the form [ ( 'G', ['Harry Potter'] ) , ...]
'''
numberOfNames = file_text[0]
splitByHouseAndName = [(line.split(' ', 1)[0], line.split(' ', 1)[1:]) for line in file_text[1:]]

'''
Create a dictionary of lists, where each name is added to the list
corresponding to that house key
'''
houses = {}
for line in splitByHouseAndName:
    if line[0] in houses:
        houses[line[0]] = houses[line[0]] + line[1]
    else:
        houses[line[0]] = line[1]

'''
-   Sort the houses by key, then print out the full name of the house
-   Sort the list associated withb that house in the dictionary, then iterate
    through the list and print it
'''
sorted_houses = sorted(houses.items())
for i in range(0, len(sorted_houses)):
    if sorted_houses[i][0] == 'G':
        print("Gryffindor:")
    elif sorted_houses[i][0] == 'H':
        print("Hufflepuff:")
    elif sorted_houses[i][0] == 'R':
        print("Ravenclaw:")
    else:
        print("Slytherin:")

    sorted_houses[i][1].sort()

    for member in sorted_houses[i][1]:
        print member

    if i != len(sorted_houses) - 1:
        print("")
