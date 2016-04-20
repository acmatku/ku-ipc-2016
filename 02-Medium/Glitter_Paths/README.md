Read from stdin two lines of paired integers, and additional lines representing a maze. The first line of input is a space-separated pair of integers representing the dimensions of a maze. The second line is a space-separated pair of integers representing the coordinate of the entry point in the maze (*note* that the maze indices are indexed at 0). The successive lines represent a maze to navigate. # represents a wall. E and R represent Emeralds and Rubies. As you navigate the maze, you can only proceed past an Emerald if you have most recently seen a Ruby, and you can only proceed past a Ruby if you have most recently seen an Emerald. 

Mark your progress with X's as you traverse the maze. Output the shortest path through the maze.

Sample input:
```
7 11
1 1
###########
#S###G   E#
# ### ### #
#R   R   R#
# ### ### #
#E   R   E#
###########
```

Sample output:
```
###########
#X###GXXXX#
#X### ###X#
#X   R   X#
#X### ###X#
#XXXXXXXXX#
###########
```
