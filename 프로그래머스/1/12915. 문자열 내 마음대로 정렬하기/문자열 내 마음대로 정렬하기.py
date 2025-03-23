# def solution(strings, n):
#     return sorted(strings, key=lambda x:(x[n],x))



def solution(strings, n):
    def my_key(x):
        return (x[n], x)
    return sorted(strings, key=my_key)
