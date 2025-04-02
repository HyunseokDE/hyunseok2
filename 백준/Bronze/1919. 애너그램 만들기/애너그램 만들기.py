
# 입력 받기
a = input().strip()
b = input().strip()

# 알파벳 개수만큼 배열 생성 (a~z: 총 26글자)
count_a = [0] * 26
count_b = [0] * 26

# 문자열 a에서 각 문자 세기
for char in a:
    index = ord(char) - ord('a')
    count_a[index] += 1

# 문자열 b에서 각 문자 세기
for char in b:
    index = ord(char) - ord('a')
    count_b[index] += 1

# 차이의 절댓값을 누적해서 제거할 문자 수 구하기
total_deletions = 0
for i in range(26):
    total_deletions += abs(count_a[i] - count_b[i])

print(total_deletions)
