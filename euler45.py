import math

def triangle(n):
    return n*(n+1)/2

def isPentagonal(p):
    n = (1 + math.sqrt(24*p+1))/6
    if n == int(n):
        return True
    return False
def isHexagonal(p):
    n = (1 + math.sqrt(8*p+1))/4
    if n == int(n):
        return True
    return False

for n in range(286,1000000):
    p = triangle(n)
    if isPentagonal(p) and isHexagonal(p):
        print(p)
        break
