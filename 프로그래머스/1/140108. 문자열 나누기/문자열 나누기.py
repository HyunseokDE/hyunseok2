def solution(s):
    answer = 0
    x_count = 0
    other_count = 0
    for i in range(len(s)):
        
        if x_count == 0:
            x = s[i]
                
        if x == s[i]:
            x_count += 1
        else:
            other_count += 1
            
        if x_count == other_count:
            answer += 1
            x_count, other_count = 0,0
            
        elif i == len(s)-1:
                answer += 1
                continue
    return answer