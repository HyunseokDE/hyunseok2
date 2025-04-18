import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for i in range(N):
    command = sys.stdin.readline().rstrip()

    if command.split()[0] == 'push':
        stack.append(int(command.split()[1]))

    elif command.split()[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command.split()[0] == 'size':
        print(len(stack))

    elif command.split()[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
            
    elif command.split()[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)