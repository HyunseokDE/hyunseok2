table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total = 0.0
total_hak = 0.0
for i in range(20):
    subject, hak, score = input().split()
    if score == 'P':
        continue
    total += float(hak) * table[score]
    total_hak += float(hak)
result = total / total_hak
print(f'{result:.6f}')