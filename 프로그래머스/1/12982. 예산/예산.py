def solution(d, budget):
    answer = 0
    d = sorted(d)
    sum = 0
    for i in range(len(d)):
        sum += d[i]
        if budget >= sum:
            answer += 1
            if i == len(d)-1:
                return answer
        else:
            return answer