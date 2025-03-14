def solution(wallpaper):
    answer = []
    x_list = []
    y_list = []
    x,y = 0,0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] =='.':
                continue
            elif wallpaper[i][j] == '#':
                x = i+1
                y = j+1
                x_list.append(x)
                y_list.append(y)
    answer = [min(x_list)-1,min(y_list)-1,max(x_list),max(y_list)]
    return answer