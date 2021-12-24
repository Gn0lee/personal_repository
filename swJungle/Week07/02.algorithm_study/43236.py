from collections import deque

def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks = [0] + rocks + [distance]
    term_dis = [0] * (len(rocks)-1)
    
    for i in range(len(rocks)-1):
        term_dis[i] = rocks[i+1] - rocks[i]
    
    start , end = 0, distance
    
    while start <= end:
        mid = (start + end)//2
        
        tmp_list = deque([i for i in term_dis])
        tmp = 0
        count = 0
        
        while tmp_list:
            now = tmp_list.popleft()
            
            if tmp_list and now < mid:
                tmp_list[0] += now 
                count += 1
            elif not tmp_list and now < mid:
                count += 1
            else:
                continue
    
        if count > n:
            end = mid - 1
        elif count <= n:
            start = mid + 1
            answer = mid
    
    
    return answer