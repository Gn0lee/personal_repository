def solution(progresses, speeds):
    from collections import deque
    
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        count = 1
        
        now_prog = progresses.popleft()
        now_speed = speeds.popleft()
        if (100 - now_prog) % now_speed == 0:
            finish_day = (100 - now_prog) // now_speed
        else:
            finish_day = (100 - now_prog) // now_speed + 1
        
        for i in range(len(progresses)):
            chk_prog , chk_spd = 100 - progresses[i], speeds[i]
            
            if chk_prog % chk_spd == 0:
                chk_day = chk_prog // chk_spd
            else:
                chk_day = chk_prog // chk_spd + 1
            if chk_day <= finish_day:
                count += 1
            else:
                break
            
        for _ in range(count - 1):
            progresses.popleft()
            speeds.popleft()
        
        answer.append(count)
    
    
    return answer