def solution(pegs):
    distances = [pegs[i+1] - pegs[i] for i in range(len(pegs) - 1)]
    sum_distance = sum((-1) ** i * distances[i] for i in range(len(distances)))

    if len(pegs) % 2:
        output = [sum_distance * 2, 1]
    else:
        if sum_distance % 3 == 0:
            output = [sum_distance * 2 / 3, 1]
        else:
            output = [sum_distance * 2, 3]

    for item in get_sizes(output[0] / output[1], distances):
        if item < 1:
            return [-1, -1]
    return output


def get_sizes(radius, distances):
    sizes = [radius]
    for item in distances:
        sizes.append(item - sizes[-1])
    return sizes


print(solution([4, 17, 50]))
print(solution([4, 30, 50]))
print(solution([4, 9, 12, 14]))
print(solution([4, 24, 56, 91, 110]))
