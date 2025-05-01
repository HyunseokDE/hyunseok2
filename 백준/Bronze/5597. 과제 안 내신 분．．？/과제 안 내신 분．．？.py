import sys

n = 30

total = list(range(1,n+1))

for i in range(28):
    student = int(sys.stdin.readline().rstrip())
    total.remove(student)

print(min(total))
print(max(total))