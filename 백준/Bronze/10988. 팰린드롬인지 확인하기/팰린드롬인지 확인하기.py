import sys

word = sys.stdin.readline().rstrip()

if word == word[::-1]:
    j = 1
else:
    j = 0
    
print(j)
