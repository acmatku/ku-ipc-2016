'''
ACM@KU Intramural Programming Competition 2016

Author: Stefan Mendoza
Problem: Easy - Impure Letters
'''

import sys

file_text = [line.strip() for line in sys.stdin.readlines()]
word_count = int(file_text[0])
words = file_text[1:]


for i in range(0, word_count):
    if 'I' in words[i] and 'P' in words[i] and 'C' in words[i]:
        i_indices = []
        p_indices = []
        c_indices = []

        for j in range(0, len(words[i])):
            if words[i][j] == 'I':
                i_indices.append(j)
            elif words[i][j] == 'P':
                p_indices.append(j)
            elif words[i][j] == 'C':
                c_indices.append(j)

        i_index = i_indices[0]
        p_indices = [index for index in p_indices if index > i_index]

        if p_indices == []:
            print("INVALID")
        else:
            p_index = min(p_indices)
            c_indices = [index for index in c_indices if index > p_index]

            if c_indices == []:
                print("INVALID")
            else:
                c_index = min(c_indices)
                print((c_index - 1 - p_index) + (p_index - 1 - i_index))
    else:
        print("INVALID")
