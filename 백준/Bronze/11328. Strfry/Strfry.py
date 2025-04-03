from collections import Counter
N = int(input())
for _ in range(N):
    A, B = input().split()
    if Counter(A) == Counter(B):
        print('Possible')
    else:
        print("Impossible")