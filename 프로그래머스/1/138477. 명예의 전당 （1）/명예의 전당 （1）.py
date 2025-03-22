def solution(k, score):
    answer = []
    k_list = []
    
    for s in score:
        if len(k_list) < k:
            k_list.append(s)
        else:
            if s > min(k_list):
                k_list.remove(min(k_list))
                k_list.append(s)
        answer.append(min(k_list))
        
    return answer
