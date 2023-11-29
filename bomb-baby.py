def solution(x, y):
    M, F = int(x), int(y)
    gen = 0

    while not (M == 1 and F == 1):
        if M < 1 or F < 1 or M == F:
            return 'impossible'
        if M == 1 or F == 1:
            gen += max(M, F) - 1
            return gen

        if M > F:
            gen += M // F
            M %= F
        elif F > M:
            gen += F // M
            F %= M

    return str(gen)
