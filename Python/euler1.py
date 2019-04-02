# Euler Project проблема 1
# найти сумму чисел от 1 до 1000, делящихся на 3 или 5
sum = 0
for i in range(3,1000,3):
    sum += i
for j in range(5,1000,5):
    if j%3 != 0:
        sum += j
print(sum)
