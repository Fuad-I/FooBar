from functools import reduce

true_states = {((0, 0), (1, 0)), ((0, 1), (0, 0)), ((1, 0), (0, 0)), ((0, 0), (0, 1))}
false_states = {((1, 1), (0, 0)), ((1, 0), (1, 0)), ((0, 0), (1, 1)), ((0, 1), (1, 1)), ((0, 1), (0, 1)), ((1, 1),
                (0, 1)), ((1, 0), (0, 1)), ((1, 1), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (1, 1)), ((0, 0), (0, 0)),
                ((0, 1), (1, 0))}


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


test = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False],
        [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False],
        [True, False, True, False, False, True, True, True]]

test2 = [[True, True, False, True, False, True, False, True, True, False],
         [True, True, False, False, False, False, True, True, True, False],
         [True, True, False, False, False, False, False, False, False, True],
         [False, True, False, False, False, False, True, True, False, False]]

print(solution(test), solution(test2))
