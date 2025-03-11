def oven(h,m,o):
    end_h = h
    end_m = m + o
    
    if (end_m) > 59:
        end_h += (end_m) // 60
        end_m = (end_m) % 60
    if end_h > 23:
        end_h = end_h % 24
    end = str(end_h) + ' ' + str(end_m)
    return end

string=input()
h,m = int(string.split(' ')[0]),int(string.split(' ')[1])
o = int(input())
print(oven(h,m,o))