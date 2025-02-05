def solution(sizes):
    answer = 0
    max1, m1 = 0,0
    max2, m2 = 0,0 
    
    for na in sizes:
        na = na.sort()
    
    for na in sizes:
        m1 = na[0]
        m2 = na[1]
        if m1 > max1:
            max1 = m1
        if m2 > max2:
            max2 = m2
    
    answer = max1 * max2
    return answer