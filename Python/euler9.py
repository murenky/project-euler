# Euler Project �������� 9
# ����� ������������ abc, ���� a+b+c=1000 � a^2+b^2=c^2
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if a*a + b*b == c*c:
                if a+b+c == 1000:
                    print(a,b,c,a+b+c)