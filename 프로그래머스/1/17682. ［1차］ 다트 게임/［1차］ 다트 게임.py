def solution(d):
    answer = 0
    scores = []
    score = 0
    i = 0
    s = 0
    while len(d) > i:
        if d[i:i+2] == '10':
            score = int(d[i:i+2])
            i += 2
        elif d[i] in ['1','2','3','4','5','6','7','8','9','0']:
            score = int(d[i])
            i += 1
        
        
        if d[i] == 'S':
            score = score ** 1
        elif d[i] == 'D':
            score = score ** 2
        elif d[i] == 'T':
            score = score ** 3
        i += 1
        
        if i < len(d) and d[i] in ['*', '#']:
            if d[i] == '#':
                score *= -1
            elif d[i] == '*':
                score *= 2
                if len(scores) >= 1:
                    scores[-1] *= 2
            i += 1
        
        scores.append(score)
        s += 1
    return sum(scores)

'''def solution(d):
    answer = 0
    s=[]
    t=0
    c = 0
    for i in range(len(d)):
        if d[i] in ['1','2','3','4','5','6','7','8','9','0','10']:
            
            if len(d[t:i]) == 1:
                continue
            else:
                s.append((d[t:i]))
                t = i
            if len(s) == 3:
                s.append(d[i:])
    del s[0]
    print(s)
    temp = 0
    temp_p = 0
    
    for j in range(3):
        
        temp = int(s[j][0])
        if s[j][1] == '0':
            temp = int(s[j][:2])
        
        for w in range(1,len(s[j])):
            if s[j][w] == 'T':
                temp = temp ** 3
            elif s[j][w] == 'D':
                temp = temp ** 2
            elif s[j][w] == 'S':
                temp = temp ** 1
            elif s[j][w] == '*':
                temp *= 2
                answer -= temp_p
                temp += temp_p * 2
            elif s[j][w] == '#':
                temp *= -1
                
        temp_p = temp
        print(temp,temp_p)
        answer += temp
    return answer'''