def solution(left, right):
    answer = 0
    lis = list(range(left,right+1,1))
    
    for n in lis:
        c = 0
        for i in range(1,n+1):
            if n % i == 0:
                c += 1
        if c % 2 == 0:
            answer += n
        else:
            answer -= n
                
    return answer