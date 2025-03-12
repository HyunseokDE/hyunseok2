def solution(a, b):
    answer = 0
    x = 0
    if b < a:
        answer = a
        a = b
        b = answer
    print(a, b)
    for i in range(a,b+1):
        x += i
    return x