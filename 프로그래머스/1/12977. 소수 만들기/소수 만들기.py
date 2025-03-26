from itertools import combinations

def prime(x):
    c = 0
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            c += 1
    if c == 1:
        return True
    
def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    for i in arr:
        if prime(sum(i)):
            answer += 1
    
    return answer

