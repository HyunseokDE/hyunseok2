N = input().split()
N,K = N
P = []
c=0
# P = ['1 1', '0 1', '1 1', '0 2', '1 2', '0 2', '0 3', '1 3', '1 4', '1 3', '1 3', '0 6', '1 5', '0 5', '1 5', '1 6']
# N = 16
# K = 2
for _ in range(int(N)):
    S = input()
    P.append(S)
from collections import Counter
Count = list(Counter(P).values())
for i in Count:
    if i <= 2:
        c += 1
    else:
        c += (i+1)//2
print(c)