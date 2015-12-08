# Проблема 52: найти наименьшее целое x, такое что 2x, 3x, 4x, 5x и 6x содержат одни и те же цифры
def same_digits(a,b):
    sa = str(a)
    sb = str(b)
    if len(sa) == len(sb):
        if sorted(list(sa)) == sorted(list(sb)):
            return True
    return False

print('start')
for i in range(100000,1000000):
    c = 0
    for j in range(2,7):
        if same_digits(i,i*j):
            c += 1
    if c == 5:
        print(i)
        break
print('end')