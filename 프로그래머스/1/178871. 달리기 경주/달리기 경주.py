def solution(players, callings):
    # "선수 이름" : 등수 dictionary 만들기
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    # calling을 보고 현재 등수를 dic에서 참조 후 players의 등수 바꾸기
    for call in callings:
        current = dic[call]
        players[current],players[current-1] = players[current-1],players[current]
        
        dic[players[current]] = current
        dic[players[current-1]] = current-1
        
    return players