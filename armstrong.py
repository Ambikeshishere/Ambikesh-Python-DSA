def solution(n):
    num = n
    total = 0
    nod = len(str(n))
    while n > 0:
        ld = n % 10
        total += ld ** nod
        n //= 10
    return total == num

print(solution(153))
print(solution(451))