from collections import Counter

alp = input().upper()

n_dic = Counter(alp) # Counter({'z': 2, 'a': 1})
n_list = list(n_dic.items())

max_alp_list = []

max_c = max(n_dic.values())

for i in range(len(n_list)):
    al, count = n_list[i]
    if max_c == count:
        max_alp_list.append(al)

if len(max_alp_list) > 1:
    print('?')
else:
    print(max_alp_list[0])


