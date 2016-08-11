# Solution to Project Euler Problem 10

def isPrime(x, primes):
    for i in primes:
        if x%i==0:
            return False
        if i > x*x:
            return False
    return True

MAX = 2000000

i = 2
sum = 0
primes = list()

while(i<MAX):
    if isPrime(i, primes):
        sum+=i
        primes.append(i)
    i+=1
    if i%10000==0:
        print(i)

print(sum)
