def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        ld = n % 10
        rev = rev * 10 + ld
        n //= 10
    return temp == rev

n = int(input("Enter a number: "))
print(is_palindrome(n))
