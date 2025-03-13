def solution(n):
    answer = []
    a = ''
    for i in str(n):
        answer.append(int(i))
        
    answer = sorted(answer)
    s = len(answer)
    
    for an in range(len(answer)):
        s -= 1
        a += str(answer[s])
    return int(a)