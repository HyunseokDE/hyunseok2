# def solution(number, limit, power):
#     l = []
#     for i in range(1,number+1):
#         c = 0
#         for j in range(1,i+1):
#             if (i % j == 0):
#                 c += 1
#         l.append(c)
    
#     for w in range(len(l)):
#         if l[w] > limit:
#             l[w] = power
#     return sum(l)    >>>>>>>> 시간초과

def solution(number, limit, power):
    l = []
    # 범위를 sqrt로 줄임
    for i in range(1,number+1):
        c = 0
        
        for j in range(1,int(i**0.5)+1):
            if (i % j == 0):
                c += 1
                if j**2 != i:
                    c += 1
                
        if c > limit:
            c = power
            
        l.append(c)            
    return sum(l)

