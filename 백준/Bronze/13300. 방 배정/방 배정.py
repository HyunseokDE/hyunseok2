from collections import Counter

N_K = input().split()
N, K = map(int, N_K)
P = []

for _ in range(N):
    S = input()
    P.append(S)

c = 0
Count = list(Counter(P).values())
for i in Count:
    c += (i + int(K) - 1) // int(K)
print(c)
