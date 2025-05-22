import sys

mat = []
for _ in range(5):
    word = sys.stdin.readline().rstrip()
    mat.append(word)

maximum = max(len(row) for row in mat)

for i in range(5):
    if len(mat[i]) < maximum:
        mat[i] = mat[i]+ (" " * (maximum-len(mat[i])))
    
for x in range(maximum):
    for y in range(5):
        if mat[y][x] != " ":
            print(mat[y][x], end='')
