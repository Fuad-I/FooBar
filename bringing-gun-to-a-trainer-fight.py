from math import atan2, ceil


def get_reflections(position, dimensions, distance):
    width, height = dimensions
    x0, y0 = position
    x_values, y_values = [x0, -x0], [y0, -y0]
    dx, dy = width - x0, height - y0

    num_horizontal_reflections = int(ceil((x0 + distance) / width))
    num_vertical_reflections = int(ceil((y0 + distance) / height))

    x, y = x0, y0
    for i in range(num_horizontal_reflections):
        x += 2 * x0 if i % 2 else 2 * dx
        x_values.extend([x, -x])

    for i in range(num_vertical_reflections):
        y += 2 * y0 if i % 2 else 2 * dy
        y_values.extend([y, -y])

    reflected_coordinates = list()
    for x_pos in x_values:
        for y_pos in y_values:
            reflected_coordinates.append([x_pos, y_pos])

    return reflected_coordinates


def squared_distance(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def solution(dimensions, your_position, trainer_position, distance):
    your_positions = [(point[0], point[1], 0) for point in get_reflections(your_position, dimensions, distance)]
    your_positions.remove((your_position[0], your_position[1], 0))
    trainer_positions = [(point[0], point[1], 1) for point in get_reflections(trainer_position, dimensions, distance)]

    points = your_positions + trainer_positions
    points.sort(key=lambda x: squared_distance(x, your_position))

    angles = set()
    count = 0
    distance_squared = distance ** 2
    for point in points:
        if squared_distance(point, your_position) <= distance_squared:
            angle = atan2(point[1] - your_position[1], point[0] - your_position[0])
            if angle not in angles:
                angles.add(angle)
                if point[2]:
                    count += 1
        else:
            break
    return count


print(solution([3, 2], [1, 1], [2, 1], 4))
print(solution([300, 275], [150, 150], [185, 100], 500))
print(solution([10, 10], [4, 4], [3, 3], 5000))
