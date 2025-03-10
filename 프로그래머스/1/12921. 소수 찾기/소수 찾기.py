import math

def solution(n):
    answer = 0

    if n < 2:
        return 0  
     
    for a in range(2, n + 1):
        sosu = True  
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                sosu = False  
                break
        if sosu:
            answer += 1  

    return answer
