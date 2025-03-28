def solution(N, stages):
    answer = []
    count = [0] * (N+2)
    print(count)
    for s in stages:
        count[s] += 1
    print(count)
    
    total_players = len(stages)
    
    fail_rates = []
    
    for stage in range(1, N + 1):
        if total_players == 0:
            fail_rates.append((stage, 0))
        else:
            fail_rate = count[stage] / total_players
            fail_rates.append((stage, fail_rate))
            
            total_players -= count[stage]
    
    fail_rates.sort(key=lambda x: x[1], reverse=True)
    
    return [stage for stage, _ in fail_rates]