def solution(n, m):
    max = 0
    min = 0
    if n > m :
        n,m = m,n
        
    for i in range(1, n+1):
        if (n % i == 0) and (m % i == 0):
            max = i
            
    for j in range(m, n*m+1):
        if (j % n == 0) and (j % m == 0):
            min = j
            return [max, min]
    