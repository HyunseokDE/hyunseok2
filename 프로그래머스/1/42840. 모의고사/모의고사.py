def solution(answers):
    answer = []
    a_answer = [1,2,3,4,5]
    b_answer = [2,1,2,3,2,4,2,5]
    c_answer = [3,3,1,1,2,2,4,4,5,5]
    
    d = len(answers)
    a_answer = a_answer * (d//5) + a_answer[:d%5]
    b_answer = b_answer * (d//8) + b_answer[:d%8]
    c_answer = c_answer * (d//10) + c_answer[:d%10]
    
    a,b,c, = 0,0,0
    for p in range(len(answers)):
        if answers[p] == a_answer[p]:
            a += 1
        if answers[p] == b_answer[p]:
            b += 1
        if answers[p] == c_answer[p]:
            c += 1
            
    dd = [a,b,c]
    for i in range(3):
        if dd[i] == max(a,b,c):
            answer.append(i+1)
            
    return sorted(answer)