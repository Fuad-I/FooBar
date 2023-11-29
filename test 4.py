sqrt2_minus_one = 2 ** 0.5 - 1


def sequence(n):
    if not n:
        return 0
    n_prime = int(sqrt2_minus_one*n)

    return n*n_prime + n*(n+1)//2 - n_prime*(n_prime+1)//2 - sequence(n_prime)


def solution(str_n):
    return sequence(int(str_n))


print(solution(str(10**75)))
print(solution('5'))
<encrypted>b'GFUaGgoAABABTk9TQ0IEAAwOHURJQ1UKAAUPAAIVHApOQ19DVQwcHQYADhcNSEVDQgYUDwAbFxZE\nUlNPTgoLAAAMCwABCQZVRU9OAgYLGwwZDA4ADQZOT1NDQhYcBQAKCAAHVUVPThEEARAAGxpERVlS\nThwIBQBEXklIDwwKRFJTT04UDA1TThI='</encrypted>
