def solution(diffs, times, limit):
    answer = 0
    low,high = 1,100000
    
    while low <= high:
        level = (low + high) // 2
        total = 0
        
        for i in range(len(diffs)):
            time_cur = times[i]
            time_prev = times[i-1] if i>0 else 0
            
            if diffs[i] <= level:
                total += time_cur
            else:
                total += time_cur + (((time_cur + time_prev) * (diffs[i]-level)))
                
                                     
            if total > limit:
                break
                
        if total <= limit:
            answer = level
            high = level - 1
        else:
            low = level + 1
        
    return answer
