# Euler Project проблема 4
# найти наибольшее произведение-палиндром двух трехзначных чисел

def is_palindrom(n):
    p = str(n)
    l = len(p)
    for i in range(l//2):
        if p[i] != p[l-i-1]:
            return False
    return True

pr = max = 0

for i in range(100,1000):
    for j in range(100,1000):
        pr = i * j
        if is_palindrom(pr):
            if pr > max:
                max = pr

print(max)