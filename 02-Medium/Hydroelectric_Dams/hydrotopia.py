'''
ACM@KU Intramural Programming Competition 2016

Author: Stefan Mendoza
Problem: Easy - Hydroelectric Dams
'''

import sys

# Open the file & read it, removing any whitespace at the end of the file
file_text = [line.strip() for line in sys.stdin.readlines()]
longest_line = max([len(line) for line in file_text])
blanks = []
generators = []
water = []
walls = []

for i in range(0, len(file_text)):
    for j in range(0, len(file_text[i])):
        if file_text[i][j] == 'W':
            water.append((i, j))
        elif file_text[i][j] == 'G':
            generators.append((i,j))
        elif file_text[i][j] == 'X':
            walls.append((i,j))
        else:
            blanks.append((i,j))

    for j in range(len(file_text[i]), longest_line):
        blanks.append((i,j))

print("Blanks:", blanks)
print("Generators:", generators)
print("Water:", water)
print("Walls:", walls)

final = []
for i in range(0, len(file_text)):
    final.append([''] * 7)
