A = int(input())
B = int(input())
C = int(input())

R = str(A * B * C)

from collections import Counter

s = Counter(R)
for i in range(10):
    if str(i) in s:
        print(s[str(i)])
    else:
        print(0)