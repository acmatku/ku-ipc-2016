import fileinput
import sys
from pdb import set_trace as st
from collections import namedtuple
import copy
import pprint

N = 1
BOARD_SIZE = 10
point = namedtuple('point', ['x', 'y'])
possible_knight_moves = [point(1,2),
                         point(-1, 2),
                         point(2, 1),
                         point(2, -1),
                         point(1, -2),
                         point(-1, -2),
                         point(-2, 1),
                         point(-2, -1)]

def add_points(q1, q2):
    return (q1.x + q2.x, q1.y + q2.y)

def under_knight_attack(q1, q2):
    return any([x == q2 for x in [add_points(q1, y) for y in possible_knight_moves]])

def under_bishop_attack(q1, q2):
    # if q1.y > q2.y:
    #     q1, q2 = q2, q1
    # return q1.x + q2.x == q1.y + q2.y or q1.x - q2.x == q1.y - q2.y
    return abs(q1.y - q2.y) == abs(q1.x - q2.x)

# print(under_knight_attack(point(1,1), point(3,2)))
# print(under_knight_attack(point(1,1), point(1,2)))
# print(under_bishop_attack(point(1,1), point(3,3)))
# print(under_bishop_attack(point(2,1), point(3,2)))
# print(under_bishop_attack(point(2,1), point(1,1)))
# print(under_bishop_attack(point(1,3), point(2,2)))
# print("=============================")

def under_attack(q1, q2):
    return under_bishop_attack(q1,q2) or under_knight_attack(q1, q2)
# print(under_attack(point(1,1), point(3,2)))
# print(under_attack(point(1,1), point(1,2)))
# print(under_attack(point(1,1), point(3,3)))
# print(under_attack(point(2,1), point(3,2)))
# print(under_attack(point(2,1), point(1,1)))

board1 = [point(1,1), point(2,1), point(3,1)]
board2 = [point(2,1), point(2,2), point(2,3)]
board3 = [point(2,1), point(3,1), point(1,1)]
board4 = [point(1,1), point(2,2), point(3,2)]
board5 = [point(1,1), point(2,2), point(3,3)]

def point_sort_key(x):
    return x.x*10+x.y

# print(sorted(board1, key=point_sort_key))
# print(sorted(board2, key=point_sort_key))
# print(sorted(board3, key=point_sort_key))

def any_under_attack(q, board):
    return any([under_attack(q, cur_q) for cur_q in board])

# print(any_under_attack(point(4,1), board1))
# print(any_under_attack(point(4,2), board1))

# print("=============================")
def next_points(board):
    if board == []:
        cur_x_max = 1
        cur_y_max = 0
    else:
        cur_x_max = max([i.x for i in board])
        cur_y_max = max([i.y for i in board if i.x == cur_x_max])
    solution = []
    while True:
        if cur_y_max+1 > N:
            cur_x_max += 1
            cur_y_max = 1
        else:
            cur_y_max += 1
        if cur_x_max > N:
            break
        solution.append(point(cur_x_max, cur_y_max))
    return solution


# print(next_points(board1))
# print(next_points(board2))
# print(next_points(board4))
# print(next_points(board5))
# print("=============================")

solutions = []

def solve():
    solve_helper([])

def solve_helper(cur_board):
    my_board = copy.copy(cur_board)
    if len(cur_board) == N:
        if sorted(my_board, key=point_sort_key) not in solutions:
            solutions.append(sorted(my_board, key=point_sort_key))
        return
    list_points = next_points(cur_board)
    # st()
    if len(list_points) == 0:
        return
    for cur_point in list_points:
        my_board = copy.copy(cur_board)
        if not any_under_attack(cur_point, cur_board):
            my_board.append(cur_point)
            solve_helper(my_board)



# answers = solve(BOARD_SIZE)
# first_answer = next(answers)
# print(len(list(answers)))
# print(list(enumerate(first_answer, start=1)))
for line in fileinput.input():
    N = int(line)
    solve()
    print(len(solutions))
    solutions = []
# pprint.pprint(solutions)


