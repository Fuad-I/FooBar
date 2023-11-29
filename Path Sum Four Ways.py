from math import inf


class Node:
    def __init__(self, num):
        self.num = num
        self.neighbours = list()

    def add_neighbour(self, node):
        self.neighbours.append(node)


def djikstra(matrix):
    nodes = [node for row in matrix for node in row]
    dist = dict()
    for node in nodes:
        dist[node] = inf
    dist[nodes[0]] = 0

    while nodes:
        node = min(nodes, key=lambda x: dist[x])
        nodes.remove(node)

        for neighbor in node.neighbours:
            if neighbor in nodes:
                alt = dist[node] + neighbor.num
                if alt < dist[neighbor]:
                    dist[neighbor] = alt

    return dist[matrix[-1][-1]] + matrix[0][0].num


m = []
with open('0083_matrix.txt', 'r') as file:
    for line in file:
        m.append([int(x) for x in line.split(',')])

m_nodes = [[Node(x) for x in row] for row in m]
for i in range(len(m)):
    for j in range(len(m) - 1):
        m_nodes[i][j].add_neighbour(m_nodes[i][j + 1])
        m_nodes[i][j + 1].add_neighbour(m_nodes[i][j])

        m_nodes[j][i].add_neighbour(m_nodes[j + 1][i])
        m_nodes[j + 1][i].add_neighbour(m_nodes[j][i])

print(djikstra(m_nodes))
