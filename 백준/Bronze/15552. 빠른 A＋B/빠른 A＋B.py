import sys

N= int(sys.stdin.readline().rstrip())

for i in range(N):
    nums = sys.stdin.readline().rstrip()
    a,b = int(nums.split()[0]),int(nums.split()[1])
    print(a+b)