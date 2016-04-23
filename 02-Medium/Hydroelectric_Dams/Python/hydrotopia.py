'''
ACM@KU Intramural Programming Competition 2016

Author: Stefan Mendoza
Problem: Medium - Hydroelectric Dams
'''

import sys

class Water():
    def __init__(self, x, y):
        self.row = x
        self.column = y

    """
    Determines whether water can move right through a generator
    """
    def canBePumped(self, graph):
        if (self.column > 0 and
            self.column < graph['columns'] - 3 and
            ((self.row, self.column + 1) in graph['generators']) and
            ((self.row, self.column + 2) in graph['blanks'])):
                return True
        else:
            return False

    """
    Moves a block of water right through a generator
    """
    def pump(self, graph):
        newBlanks = graph['blanks']
        newBlanks.remove((self.row , self.column + 2))
        newBlanks.append((self.row, self.column))
        graph['blanks'] = newBlanks

        newWater = graph['waters']
        newWater.remove((self.row, self.column))
        newWater.append((self.row, self.column + 2))
        graph['waters'] = newWater

        self.column = self.column + 2
        return graph

    """
    Determines whether water needs to move down to settle
    """
    def needsToSettle(self, graph):
        blanks = graph['blanks']
        return ((self.row + 1, self.column) in blanks)

    """
    Moves a block of water down
    """
    def settle(self, graph):
        newBlanks = graph['blanks']
        newBlanks.remove((self.row + 1, self.column))
        newBlanks.append((self.row, self.column))
        graph['blanks'] = newBlanks

        newWater = graph['waters']
        newWater.remove((self.row, self.column))
        newWater.append((self.row + 1, self.column))
        graph['waters'] = newWater

        self.row = self.row + 1
        return graph


"""
Generates a dictionary where the keys are the types of characters in the dam
and the values are lists of (row, column) tuples where that characters appears
"""
def generateOpenGraph(graph, rows, columns):
    blanks = []
    generators = []
    walls = []
    waters = []

    for i in range(0, rows):
        for j in range(0, columns):
            if graph[i][j] == 'G':
                generators.append((i,j))
            elif graph[i][j] == 'W':
                waters.append((i,j))
            elif graph[i][j] == 'X':
                walls.append((i,j))
            else:
                blanks.append((i,j))

        for j in range(len(graph[i]), columns):
            blanks.append((i,j))

    openGraph = {}
    openGraph['rows'] = rows
    openGraph['columns'] = columns
    openGraph['blanks'] = blanks
    openGraph['generators'] = generators
    openGraph['walls'] = walls
    openGraph['waters'] = waters
    return openGraph


if __name__ == '__main__':
    dam = [line.strip() for line in sys.stdin.readlines()]
    rows = int(dam[0].split(' ')[0])
    columns = int(dam[0].split(' ')[1])
    dam = dam[1:]

    for i in range(0, len(dam)):
        while len(dam[i]) < columns:
            dam[i] += ' '

    waters = []

    graph = generateOpenGraph(dam, rows, columns)

    for water in graph['waters']:
        waters.append(Water(water[0], water[1]))

    totalMoves = 0

    while(True in [water.canBePumped(graph) for water in waters]
          or True in [water.needsToSettle(graph) for water in waters]):
        moves = 0
        for i in range(0, len(waters)):
            while waters[i].canBePumped(graph):
                graph = waters[i].pump(graph)
                printGraph(graph, waters)
                moves += 1

            while waters[i].needsToSettle(graph):
                graph = waters[i].settle(graph)
                printGraph(graph, waters)
        totalMoves += moves

    print(totalMoves)
