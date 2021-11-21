import sys
from heapq import heappop,heappush
input = sys.stdin.readline
inf = int(1e9)
n = int(input())
m = int(input())

visited = [inf] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a , b ,cost = map(int,input().split())
    graph[a].append((cost,b))

start,end = map(int,input().split())

def dijkstra(start):
    q = []
    visited[start] = 0
    heappush(q,(0,start))
    while q:
        current_cost, now = heappop(q)

        if current_cost > visited[now]:
            continue
        for i in graph[now]:
            sum_cost = current_cost + i[0]
            if sum_cost < visited[i[1]]:
                visited[i[1]] = sum_cost
                heappush(q,(sum_cost,i[1]))

dijkstra(start)

ans = visited[end]

print(ans)
