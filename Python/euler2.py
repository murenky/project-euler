# Euler Project �������� 2
# ����� ����� ���� ������ ����� ���������, ������� 4 ���������
sum = 0
a = b = c = 1
while b <= 4000000:
    c = a + b
    if c%2 == 0:
        sum += c
    a = b
    b = c
print(sum)


