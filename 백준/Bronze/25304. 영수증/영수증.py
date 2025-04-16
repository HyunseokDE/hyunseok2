X = int(input())
N = int(input())

total = 0
for i in range(N):
    obj, price = map(int,input().split())
    total += obj*price

if X == total:
    print('Yes')
else:
    print('No')