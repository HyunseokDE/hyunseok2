a, b = map(int, input().strip().split(' '))
for i in range(b):
    c=''
    for j in range(a):
        c += '*'
    print(c)