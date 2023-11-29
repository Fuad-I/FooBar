from collections import Counter


def getGCDTable(n):
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == 1 or j == 1:
                table[i][j] = 1
                table[j][i] = 1
            elif i == j:
                table[i][j] = i
            else:
                table[i][j] = table[i][j - i]
                table[j][i] = table[i][j - i]
    return table


def gcd(x, y, gcd_table):
    return gcd_table[x][y]


def get_factorial_table(n):
    lst = [1]
    for i in range(1, n + 1):
        lst.append(i * lst[-1])
    return lst


def factorial(n, factorial_table):
    return factorial_table[n]


def get_coefficient_factor(partition, n, factorial_table):
    """ n!/(1^{i_1}i_1!2^{i_2}i_2!...n^{i_n}i_n!) """

    coefficient_factor = factorial(n, factorial_table)
    for a, b in Counter(partition).items():
        coefficient_factor //= (a ** b) * factorial(b, factorial_table)
    return coefficient_factor


def get_partitions(n):
    a = [0 for _ in range(n + 1)]
    k = 1
    y = n - 1
    partitions = list()
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            partitions.append(a[:k + 2])
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        partitions.append(a[:k + 1])

    return partitions


def solution(w, h, s):
    gcdTable, factorialTable = getGCDTable(max(w, h)), get_factorial_table(max(w, h))

    result = 0
    for partition_w in get_partitions(w):
        for partition_h in get_partitions(h):
            m = get_coefficient_factor(partition_w, w, factorialTable) * get_coefficient_factor(partition_h, h,
                                                                                                factorialTable)
            result += m * (s ** sum([sum([gcd(i, j, gcdTable) for i in partition_w]) for j in partition_h]))
    result //= (factorial(w, factorialTable) * factorial(h, factorialTable))

    return str(result)


print(solution(2, 3, 4))
