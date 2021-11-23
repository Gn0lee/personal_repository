import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque([])
    q.append(start)

    while q:
        now  = q.popleft()
        for i,t in graph[now]:
            indegree[i] -=1
            result[i] = max(result[i],result[now]+t)
            
            if indegree[i] == 0:
                q.append(i)

    
    q.append(end)

    chk = [False] *(n+1)
    cnt = 0
    while q:
        now  = q.popleft()
        for i ,t in back_graph[now]:
            if result[now] - result[i] == t:
                cnt += 1
                if not chk[i]:
                    chk[i] = True
                    q.append(i)

    return (result[end],cnt)


n = int(input())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
back_graph = [[]*(n+1) for _ in range(n+1)]
result = [0] * (n+1)
indegree = [0] * (n+1)

for _ in range(m):
    a , b, c = map(int,input().split())
    graph[a].append((b,c))
    back_graph[b].append((a,c))
    indegree[b] += 1

start , end = map(int,input().split())

max_time , cnt_road = topology_sort()
print(max_time)
print(cnt_road)