# Solution to Project Euler Problem 6

MAX = 100

sum_squares = 0
sum = 0

for i in range(1, MAX+1):
    sum += i
    sum_squares += i*i

print(sum*sum - sum_squares)
