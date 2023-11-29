from math import gcd


def get_gcd_table(n):
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


print(get_gcd_table(5))
print([[gcd(i, j) for j in range(6)] for i in range(6)])
