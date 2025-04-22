import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
current = 1 

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit(0)

print('\n'.join(result))
