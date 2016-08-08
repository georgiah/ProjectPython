# Solution to Project Euler Problem 2

MAX = 4000000
x1 = 1
x2 = 2
sum = 2

while True:
    x3 = x1 + x2
    x1 = x2
    x2 = x3

    if (x2 > MAX):
        break

    if (x2%2==0):
        sum += x2

print(sum)

