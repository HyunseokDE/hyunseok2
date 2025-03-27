def solution(babbling):
    answer = 0
    b = ['aya','ye','woo','ma']
    
    for i in range(len(babbling)):
        for j in range(len(b)):
            if b[j] in babbling[i]:
                if (b[j] * 2) in babbling[i]:
                    break
                babbling[i] = babbling[i].replace(b[j],'x')
                if len(babbling[i].replace('x','')) == 0:
                    answer += 1
                    continue
                
    return answer