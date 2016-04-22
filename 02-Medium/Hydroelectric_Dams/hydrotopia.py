'''
ACM@KU Intramural Programming Competition 2016

Author: Stefan Mendoza & Stephen Longofono
Problem: Medium - Hydroelectric Dams
'''

import sys

class Water():
    def __init__(self, x, y):
        self.isActive = True
        self.row = x
        self.column = y
        self.isSettled = True


    """
    Determines whether water can move right through a generator
    """
    def canBePumped(self, graph):
        if (self.column > 0 and
                self.column < graph['length'] - 3 and
                ((self.row, self.column + 1) in graph['generators'])):
                return True
        else:
            self.isActive = False
            return False


    """
    """
    def pump(self, graph):
        for key in graph:
            print(key, graph.get(key))
        print("\n")

        newBlanks = graph['blanks']
        newBlanks.remove((self.row , self.column + 2))
        graph['blanks'] = newBlanks

        newWater = graph['waters']
        newWater.remove((self.row, self.column))
        newWater.append((self.row, self.column + 2))
        graph['waters'] = newWater
        return graph


    """
    Determines whether water needs to move down to settle
    """
    def needsToSettle(self, graph):
        blocked = graph['generators'] + graph['walls'] + graph['waters']
        return ((self.row + 1, self.column) not in blocked)


    """
    """
    def settle(self, graph):
        newBlanks = graph['blanks']
        newBlanks.remove((self.row + 1, self.column))
        graph['blanks'] = newBlanks

        newWater = graph['waters']
        newWater.remove((self.row, self.column))
        new.append((self.row + 1, self.column))
        graph['waters'] = newWater
        return graph


"""
"""
def generateOpenGraph(graph):
    longest_line = max([len(line) for line in graph])

    blanks = []
    generators = []
    walls = []
    waters = []

    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if graph[i][j] == 'G':
                generators.append((i,j))
            elif graph[i][j] == 'W':
                waters.append((i,j))
            elif graph[i][j] == 'X':
                walls.append((i,j))
            else:
                blanks.append((i,j))

        for j in range(len(graph[i]), longest_line):
            blanks.append((i,j))

    openGraph = {}
    openGraph['length'] = longest_line
    openGraph['height'] = len(graph)
    openGraph['blanks'] = blanks
    openGraph['generators'] = generators
    openGraph['walls'] = walls
    openGraph['waters'] = waters
    return openGraph


if __name__ == '__main__':
    dam = [line.strip() for line in sys.stdin.readlines()]
    dam = dam[1:]

    waters = []

    for i in range(0, len(dam)):
        for j in range(0, len(dam[i])):
            if dam[i][j] == 'W':
                waters.append(Water(i,j))

    graph = generateOpenGraph(dam)
    totalMoves = 0

    while True in [water.isActive for water in waters]:
        moves = 0
        for i in range(0, len(waters)):
            while waters[i].canBePumped:
                graph = waters[i].pump(graph)
                moves += 1
                while waters[i].needsToSettle:
                    graph = waters[i].settle(graph)

        totalMoves += moves
        if moves == 0:
            break

    print(totalMoves)
    # print(graph['generators'])
    # print("length =", graph['length'])
    #
    # for i in range(0, len(waters)):
    #     print((waters[i].row, waters[i].column))
    #     print("Can be pumped:", waters[i].canBePumped(graph))
    #     print("Needs to settle:", waters[i].needsToSettle(graph))
    #     print("\n")
