'''
ACM@KU Intramural Programming Competition 2016

Author: Stefan Mendoza
Problem: Easy - Impure Letters
'''

import sys

# Open the file & read it, removing any whitespace at the end of the file
f = open(sys.argv[1])
file_text = f.read().strip().split('\n')

for word in file_text:
    if 'I' in word and 'P' in word and 'C' in word:
        iIndices = []
        pIndices = []
        cIndices = []
        for i in range(0, len(word)):
            if word[i] == 'I':
                iIndices.append(i)
            elif word[i] == 'P':
                pIndices.append(i)
            elif word[i] == 'C':
                cIndices.append(i)

    print(iIndices)
    print(pIndices)
    print(cIndices)
    print("\n")
