import sys

line = int(sys.stdin.readline().rstrip())

for i in range(1,line+1):
    print(f"{' '*(line-i)}{'*'*i}")