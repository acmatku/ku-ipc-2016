import sys

f = open(sys.argv[1])
file_text = f.read().strip().split('\n')

numberOfNames = file_text[0]
splitByHouseAndName = [(line.split(' ', 1)[0], line.split(' ', 1)[1:]) for line in file_text[1:]]

houses = {}

for line in splitByHouseAndName:
    if line[0] in houses:
        houses[line[0]] = houses[line[0]] + line[1]
    else:
        houses[line[0]] = line[1]

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
