from collections import defaultdict, deque
from heapq import heappop,heappush

def solution(n, s, a, b, fares):
    answer = 1e9
    graph = defaultdict(list)
    # graph1 = defaultdict(list)
    cost_start = [1e9] * (n+1)
    q1 = []

    for c,d,f in fares:
        graph[c].append([f,d])
        graph[d].append([f,c])
        # graph1[c].append([f,d])
    
    def dijkstra(start,n):
        q = []
        cost = [1e9] *(n+1)
        cost[start] = 0
        heappush(q,[0,start])
        
        while q:
            now_cost , now = heappop(q)
            
            if now_cost > cost[now]:
                continue
                
            for next_spot in graph[now]:
                cost_sum = now_cost + next_spot[0] 
                if cost_sum < cost[next_spot[1]]:
                    cost[next_spot[1]] = cost_sum
                    heappush(q,[cost_sum,next_spot[1]])
            
        return [cost[a],cost[b]]    
    
    cost_start[s] = 0
    heappush(q1,[0,s])

    while q1:
            now_cost , now = heappop(q1)
            
            if now_cost > cost_start[now]:
                continue
                
            for next_spot in graph[now]:
                cost_sum = now_cost + next_spot[0] 
                if cost_sum < cost_start[next_spot[1]]:
                    cost_start[next_spot[1]] = cost_sum
                    heappush(q1,[cost_sum,next_spot[1]])

    for i in range(1,n+1):
        if cost_start[i] == 1e9:
            continue
        x , y = dijkstra(i,n)
        answer = min(answer,x + y+ cost_start[i])
    
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))