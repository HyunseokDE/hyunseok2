import math

def solution(n):
    answer = 1

    if n == 2:
        return 1
    else:
        if n == 3:
            return 2
        else:
            for a in range(4, n+1):
                for i in range(2,int(math.sqrt(a))+1):
                    if (a%i != 0):
                        answer += 1
                        
                
                print(a)
                        
    return answer

