def solution(n):
    answer = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            answer.append(i)
    a = sum(answer)+n
    return a