def solution(common):
    answer = 0
    s1 = common[1]-common[0]
    s2 = common[2]-common[1]
    if s1 == s2:
        answer = common[-1]+s1
    else:
        s3 = common[1]/common[0]
        answer = common[-1]*s3
    return answer