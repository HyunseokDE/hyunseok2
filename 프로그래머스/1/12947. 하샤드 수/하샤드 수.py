def solution(x):
    answer = True
    h = 0
    for i in str(x):
        h += int(i)
    if x % h == 0:
        return answer
    else:
        return False