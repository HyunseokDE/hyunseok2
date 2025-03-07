def solution(clothes):
    # 종류별 개수를 딕셔너리로 저장
    dic = {}
    for name, kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
    
    # 경우의 수 계산
    total = 1
    for count in dic.values():
        total *= (count + 1)  # 각 종류마다 (입지 않음 + 의상 개수)
    
    # 모두 입지 않는 경우 제외
    answer = total - 1
    return answer