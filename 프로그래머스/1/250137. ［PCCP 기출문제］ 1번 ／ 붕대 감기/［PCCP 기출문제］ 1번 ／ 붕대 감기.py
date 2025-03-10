def solution(bandage, h, attacks):
    answer = 0
    health = h
    c = 0
    l = []
    for s in range(len(attacks)):
        l.append(attacks[s][0])   # 공격 시간 리스트
    # 회복된 채력 최대 health를 넘을 수 없음 bandage = [t, x, y]
    # attacks는 첫번째 원소 x 두 번째 원소로 피해량 계산 attacks = 
    # 시간 t / 현재 체력 health(h) / 연속 성공 횟수 c 
    for t in range(attacks[-1][0]+1):
        if t in l:  #공격 시간이 됐을 때
            h = h - attacks[l.index(t)][1] #체력 감소
            c = 0 # 연속 성공 횟수 초기화
            if h <= 0:
                return -1
            print(f'시간 {t} 현재 체력 {h} 연속 성공 {c}')
            continue
        if t > 0 and h < health: # 초기 상태 이후 and 최대 체력보다 낮을 때
            h = h + bandage[1]
            c += 1# 연속 성공 횟수 증가
        if c == bandage[0]:
            h = h + bandage[2]
            c = 0
        if h > health:
                h = health  # 회복된 체력이 최대 체력보다 높으면 안됨
        print(f'시간 {t} 현재 체력 {h} 연속 성공 {c}')
        
    return h