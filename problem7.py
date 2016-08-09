# Solution to Project Euler Problem 7

def is_prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0

    return 1

MAX = 10001
num_prime = 1
i = 2

while num_prime < MAX:
    i+=1
    if is_prime(i):
        num_prime+=1

print(i)
