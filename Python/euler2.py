# Euler Project проблема 2
# найти сумму четных членов ряда Фибоначчи, не превышающих 4 миллиона
sum = 0
a = b = c = 1
while b <= 4000000:
    c = a + b
    if c%2 == 0:
        sum += c
    a = b
    b = c
print(sum)


