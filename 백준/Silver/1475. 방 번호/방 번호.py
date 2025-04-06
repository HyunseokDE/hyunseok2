N = input()

from collections import Counter

N_n_s = N.replace('9','')
N_n_s = N_n_s.replace('6','')
nine_six = N.count('9') + N.count('6')

if len(N_n_s) != 0:
    N_s = Counter(N_n_s)
    print(max(max(N_s.values()), (nine_six+1)//2))
else:
    print((nine_six+1)//2)