def solution(t, p):
    answer = 0
    n_l = []
    for i in range(len(t)-len(p)+1):
        n_l.append(int(t[i:i+len(p)]))
        
    for j in n_l:
        if j <= int(p):
            answer += 1
    return answer