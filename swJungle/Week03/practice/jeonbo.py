# N개의 도시가 있으며 start에서 나머지 도시들로 전보를 보내려한다.
# 도시간 통로는 방향성이 있으며 start에서 출발하여 각 도시사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것이다.
# 이때 start에서 보낸 메세지를 받는 도시의 수와 모두 메세지를 받는데까지 걸리는 시간은 얼마인가?
import sys
input = sys.stdin.readline
from heapq import heappush,heappop

n , m , start = map(int,input().split())

inf = int(1e9)

visited = [inf] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    a,b,time = map(int,input().split())
    
    graph[a].append((time,b))

def jeonbo(start):

    visited[start] = 0
    q = []

    # for i in graph[start]:
    #     visited[i[1]] = i[0] 

    heappush(q,(0,start))
    while q:
        time , now = heappop(q)

        if time > visited[now]: ## 이미 갱신된 노드는 방문한 것과 같으므로 다음 반복으로 넘어간다.
            continue

        for i in graph[now]:
            time_sum = time + i[0]
            if time_sum < visited[i[1]]:
                visited[i[1]] = time_sum
                heappush(q,(time_sum,i[1]))


jeonbo(start)

ans = -1e9
cnt = 0

for i in visited:
    if i == inf:
        continue
    else:
        ans = max(ans,i)
        cnt += 1

## 시작 노드는 제외해야 한다!!
print(cnt-1 , ans , sep=" ")

