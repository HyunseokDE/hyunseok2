import math
def solution(w,h):
    answer = 1
    a = math.gcd(w,h)  # 4
    answer = (w * h) -(w + h)+a
# 3,3 > 6    9 - 1
    return answer