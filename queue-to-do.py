def xor_up_to_n(n):
    d = {0: n, 1: 1, 2: n + 1, 3: 0}
    return d[n % 4]


def xor(start, end):
    if start < 2:
        return xor_up_to_n(end)
    if start == end:
        return end
    return xor_up_to_n(end) ^ xor_up_to_n(start - 1)


def solution(start, length):
    result = 0
    j = length - 1 + start
    k = start

    for i in range(length):
        result ^= xor(k, j)
        k += length
        j += length - 1

    return result

