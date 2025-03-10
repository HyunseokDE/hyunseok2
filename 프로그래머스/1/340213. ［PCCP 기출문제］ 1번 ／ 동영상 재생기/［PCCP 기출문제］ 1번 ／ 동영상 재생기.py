def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    op_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    op_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
    
    if op_start <= pos <= op_end:
        pos = op_end
        
    for com in commands:
        if com == "prev":
            if pos < 10:
                pos = 0
            else:
                pos = pos - 10
        elif com == "next":
            if (video_len - pos) < 10:
                pos = video_len
            else:
                pos = pos + 10
        if op_start <= pos <= op_end:
            pos = op_end
    
                
    m = pos // 60
    s = pos % 60
    answer = f"{m:02}:{s:02}"

    return answer