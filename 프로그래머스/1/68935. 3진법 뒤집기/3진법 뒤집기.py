def solution(n):
    answer = 0
    na = ''
    # 3진법 변환(앞뒤 반전)
    while n > 0:
        na += str(n % 3)
        n = n // 3 
    
    # 10진법 변환
    i = len(na)-1
    index = 0
    while i >= 0:
        answer += int(na[index])*3**i
        i -= 1
        index += 1
        
    return answer