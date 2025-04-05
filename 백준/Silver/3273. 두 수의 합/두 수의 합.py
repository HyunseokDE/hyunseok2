n = int(input())
l = list(map(int, input().split()))
x = int(input())

c = 0
s = set()

for i in range(n):
    if x - l[i] in s:
        c += 1
    s.add(l[i])

print(c)

