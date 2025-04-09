Y = int(input())

def yoon(x):
    a = 0
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 != 0:
            a = 0
        else:
            a = 1
    return a

print(yoon(Y))