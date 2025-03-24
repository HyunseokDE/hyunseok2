def solution(a, b):
    answer = ''
    # 2016 > 366일
    cal = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    for i in range(a-1):
        day += cal[i]
    day += b
    
    answer = week[(day % 7) - 1]
    return answer