def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    answer = arr[:arr.index(min(arr))]+arr[arr.index(min(arr))+1:]
    return answer