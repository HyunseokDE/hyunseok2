def solution(s, skip, index):
    answer = ''
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # 알파벳과 숫자 매핑
    al_num = {}
    num_al = {}
    for i in range(len(a)):
        al_num[a[i]] = i
        num_al[str(i)] = a[i]
    
    # skip 문자들의 숫자 리스트
    skip_r = set(al_num[w] for w in skip)  # 더 빠른 검색을 위해 set 사용
    
    # 각 문자 처리
    for j in s:
        current_pos = al_num[j]
        steps = index  # 이동해야 할 총 칸 수
        new_pos = current_pos
        
        # index만큼 이동하면서 skip 문자 건너뛰기
        while steps > 0:
            new_pos = (new_pos + 1) % 26  # 다음 위치로 이동
            if new_pos not in skip_r:  # skip 문자가 아니면
                steps -= 1  # 한 칸 이동한 것으로 카운트
        
        answer += num_al[str(new_pos)]
    
    return answer

# 테스트
print(solution("aukks", "wbqd", 5))          # "happy" 출력
print(solution("z", "a", 1))                 # "b" 출력
print(solution("klmnopqrstuvwxyz", "abcdefghij", 20))  # "opqrstuvwxyzklmn" 출력