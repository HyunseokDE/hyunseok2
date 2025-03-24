def to_bin(x, n):
    bin = ''
    while x > 0:
        bin += str(x%2)
        x = x//2
    bin = bin[::-1]
    if len(bin) < n:
        bin = '0'*(n-len(bin)) + bin
    return bin

def solution(n, arr1, arr2):    
    # 이진수 변환하며 arr1_bi, arr2_bi로 저장
    arr1_bi = [to_bin(i,n) for i in arr1]
    arr2_bi = [to_bin(j,n) for j in arr2]
    
    # answer에 공백을 n * n 으로 만듦
    answer = []
    
    #arr1_bi, arr2_bi를 동시에 들고와 비교하며 sharp 생성
    sharp = ''
    for a,b in zip(arr1_bi,arr2_bi):
        sharp = ''
        for index in range(n):
            if a[index] == '1' or b[index] == '1':
                sharp += '#'
            else:
                sharp += ' '
        answer.append(sharp)
    return answer