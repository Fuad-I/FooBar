def sieve(n):
    lst = [i for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if lst[i]:
            for j in range(i**2, n+1, i):
                lst[j] = 0
    return ''.join([str(item) for item in lst if item][1:])


def solution(n):
    i = 2*n
    if n < 11:
        i = 11
    temp = sieve(i)
    while True:
        if len(temp) < n+6:
            i = i * 2
            temp = sieve(i)
        else:
            break

    return temp[n:n+5]

