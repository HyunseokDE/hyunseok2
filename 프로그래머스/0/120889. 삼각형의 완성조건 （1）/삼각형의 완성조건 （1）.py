def solution(sides):
    answer = 2
    sorted_sides = sorted(sides)
    
    if sorted_sides[0] + sorted_sides[1] > max(sorted_sides):
        answer = 1
    
    return answer