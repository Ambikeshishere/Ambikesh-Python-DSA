import math


def solution(n):
    from math import sqrt
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

print(solution(12480))
