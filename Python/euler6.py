# Euler Project �������� 6
# ����� ������� ����� ��������� ����� ������ ��� ����������� ����� � ������ �� ���������
sum = sum_sq = sq_sum = 0
for i in range(1,101):
    sum += i
    sum_sq += i*i
sq_sum = sum * sum
print(sq_sum - sum_sq)
