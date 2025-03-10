# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if i-1 < 0:
#             continue
#         if (arr[i] != arr[i-1]):
#             answer.append(arr[i])
#     return answer

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not len(answer):
            answer.append(arr[i])
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer
    