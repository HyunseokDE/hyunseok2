import sys

K = int(sys.stdin.readline().rstrip())

s = []

for i in range(K):
    o = int(sys.stdin.readline().rstrip())
    if o == 0:
        s.pop()
    else:
        s.append(o)

print(sum(s))
