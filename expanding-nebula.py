from itertools import permutations
from functools import reduce

true_states = set()
false_states = set()
for item in permutations((1, 0, 0, 0)):
    true_states.add((item[:2], item[2:]))
for item in (*permutations((1, 1, 0, 0)), *permutations((1, 1, 1, 0))):
    false_states.add((item[:2], item[2:]))
false_states.add(((0, 0), (0, 0)))
false_states.add(((1, 1), (1, 1)))


def check(state1, state2):
    output = set()
    for item1 in state1:
        for item2 in state2:
            if item1[-1] == item2[0]:
                output.add(item1 + (item2[1],))

    return output


def get_column(array, num):
    return [pair[num] for pair in array]


def get_image(col1, col2):
    output = set()
    for item1 in col1:
        for item2 in col2:
            if get_column(item1, -1) == get_column(item2, 0):
                output.add(tuple(item1[i] + (item2[i][1],) for i in range(len(item1))))
    return output


def solution(g):
    new_lst = [[true_states if x else false_states for x in row] for row in g]
    cols = list()
    for row in zip(*new_lst):
        cols.append(reduce(lambda a, b: check(a, b), row))
    output = reduce(lambda a, b: get_image(a, b), cols)
    return len(output)