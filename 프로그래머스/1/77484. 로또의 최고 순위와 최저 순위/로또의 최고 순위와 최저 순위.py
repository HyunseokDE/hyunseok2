def solution(lottos, win_nums):
    answer = []
    count = 0
    
    for i in range(6):
        if lottos[i] in win_nums:
            count += 1
    zero = lottos.count(0)
    maxi = 7-count-zero
    mini = 7-count
    
    if count < 2:
        mini = 6
        if count == 0 and zero == 0:
            maxi = 6
    answer=[maxi,mini]
    return answer