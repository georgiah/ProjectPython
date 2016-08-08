# Solution to Project Euler Problem 4

MAX = 999
MIN = 100

max_palindrome = 0

for i in range(MIN, MAX+1):
    for j in range(MIN, MAX+1):
        string_num = str(i*j)
        if string_num == string_num[::-1]:
            if i*j > max_palindrome:
                max_palindrome = i*j

print(max_palindrome)
