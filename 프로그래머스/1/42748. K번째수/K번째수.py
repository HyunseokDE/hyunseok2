def solution(array, commands):
    answer = []
    s=[]
    for com in commands:
        s = array[com[0]-1:com[1]]
        s.sort()
        answer.append(s[com[2]-1])
    return answer