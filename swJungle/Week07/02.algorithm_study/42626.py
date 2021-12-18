from heapq import heappush, heappop,heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    chk = True
    while scoville:
        now = scoville[0]
        
        if now >= K:
            break
        elif len(scoville) < 2:
            chk = False
            break
        else:
            lowest = heappop(scoville)
            lowest_2nd = heappop(scoville)
            heappush(scoville,(lowest+lowest_2nd*2))
            answer += 1 
    
    if not chk:
        answer = -1
        
    return answer