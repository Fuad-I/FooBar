from math import gcd


class Node:
    def __init__(self, num):
        self.num = num
        self.nums_list = list()

    def loops(self, lst):
        self.nums_list = [x for x in lst if check(x.num, self.num)]

    def __lt__(self, other):
        return len(self.nums_list) < len(other.nums_list)


def check(x, y):
    n = (x + y) // gcd(x, y)
    return bool(x != y and (n & (n - 1)))


def solution(banana_list):
    lst = [Node(x) for x in banana_list]
    for node in lst:
        node.loops(lst)

    unpaired = 0
    while lst:
        if not max(len(x.nums_list) for x in lst):
            break

        node1 = min(lst)
        while not node1.nums_list:
            lst.remove(node1)
            node1 = min(lst)
            unpaired += 1
        node2 = min(node1.nums_list)

        for node in lst:
            if node1 in node.nums_list:
                node.nums_list.remove(node1)
            if node2 in node.nums_list:
                node.nums_list.remove(node2)

        lst.remove(node1)
        lst.remove(node2)

    return len(lst) + unpaired