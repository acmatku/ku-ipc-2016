from itertools import permutations
from collections import namedtuple
import pprint
import n_princesses
point = namedtuple('point', ['x', 'y'])
N = 5
points = [point(x,y) for x in range(1,N+1) for y in range(1,N+1)]
# pprint.pprint(list(permutations(points, N)))
# print(list(permutations(points, N)))
# print(len(list(permutations(points, N))))
solutions = []

def valid_board(board):
    # n_princesses.st()
    for i in board:
        all_but = [x for x in board if x != i]
        if n_princesses.any_under_attack(i, all_but):
            return False
    return True


for solution in permutations(points, N):
    solution = list(solution)
    if valid_board(solution):
        if sorted(solution, key=n_princesses.point_sort_key) not in solutions:
            solutions.append(sorted(solution, key=n_princesses.point_sort_key))

print(len(solutions))


