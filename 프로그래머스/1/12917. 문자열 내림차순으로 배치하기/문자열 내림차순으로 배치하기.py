def solution(s):
    answer = ''
    # for i in range(0,len(s)):
    #     answer.append(s[i])
    s = sorted(s, reverse = True)
    for i in s:
        answer += i
    return answer