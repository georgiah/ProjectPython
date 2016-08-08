# Solution to Project Euler Problem 5

MAX = 20

divisible = False
num = MAX

while (not divisible):
    divisible = True
    for i in range(2, MAX):
        if num%i != 0:
            divisible = False
            break
    num += 2

print(num-2)
         
