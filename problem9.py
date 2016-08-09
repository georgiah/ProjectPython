# Solution to Project Euler Problem 9

def triplet():
    for a in range(2,1000):
        for b in range(a,1000):
            for c in range(b,1000):
                if (a*a + b*b == c*c):
                    if a+b+c == 1000:
                        return(a*b*c)

print(triplet())
