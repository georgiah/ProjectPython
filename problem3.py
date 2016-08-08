# Solution to Project Euler Problem 3

def isPrime(x):
    for i in range (2, x//2):
        if x%i==0:
            return False
    return True

num = 600851475143

for j in range(2, num//2):
    if (num%j==0):
        print(j," is Factor")
        if isPrime(num//j):
            break

print(num/j)
