def solution(name, yearning, photo):
    answer = []
    # for i in range(len(name)):
    #     ny[name[i]] = yearning[i]
    ny = {name[i]:yearning[i] for i in range(len(name))}

    for photo_i in photo:
        inter = set(name) & set(photo_i)
        score = sum(ny[person] for person in inter)
        answer.append(score)
    return answer