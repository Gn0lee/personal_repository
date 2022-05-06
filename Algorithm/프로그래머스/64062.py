def solution(stones, k):
    
    start = 1
    end = max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        cnt_step = 0
        chk = False
        for stone in stones:
            if cnt_step == k:
                chk = True
                break
            if stone <= mid:
                cnt_step += 1
            else:
                cnt_step = 0
        if chk or cnt_step == k:
            end = mid -1
        else:
            start = mid + 1
    
    
    return start