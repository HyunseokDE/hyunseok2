from collections import Counter

S = input()
S_count = Counter(S)

for i in range(97,123):
    if chr(i) in S:
        print(S_count[chr(i)],end=' ')
    else:
        print(0,end=' ')
    
print()
            