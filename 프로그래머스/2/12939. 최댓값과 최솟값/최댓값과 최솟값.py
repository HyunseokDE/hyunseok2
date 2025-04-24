def solution(s):
    s = list(s.split())
    for i in range(len(s)):
        s[i] = int(s[i])
    answer = f"{min(s)} {max(s)}"
    return answer