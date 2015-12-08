# Euler Project проблема 2
# найти сумму всех четных чисел Фибоначчи, меньших 4 миллионов
sum = 0
a = b = c = 1
while b <= 4000000:
    c = a + b
    if c%2 == 0:
        sum += c
    a = b
    b = c
print(sum)


