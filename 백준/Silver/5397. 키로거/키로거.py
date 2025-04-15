import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    left = []
    right = []
    pw = input().strip()

    for ch in pw:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)

    print(''.join(left + right[::-1]))
