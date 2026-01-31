n = input("Enter a number: ")
n = int(n)
num = n
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)