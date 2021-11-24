import sys
from heapq import heappush,heappop
input = sys.stdin.readline


inf = int(1e9)

def dijkstra(start):

    visited = [inf] * (n+1)
    visited[start] = 0
    q = []

    heappush(q,[0,start])

    while q:
        dist , now = heappop(q)
        
        if dist > visited[now]:
            continue

        for d,i in graph[now]:
            sum_dist = d + dist
            if sum_dist < visited[i]:
                visited[i] = sum_dist
                heappush(q,[sum_dist,i])
    
    return visited

n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]


for _ in range(e):
    a , b ,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

v1 , v2 = map(int,input().split())

total_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

v1_path = total_dist[v1] + v1_dist[v2] + v2_dist[n]
v2_path = total_dist[v2] + v2_dist[v1] + v1_dist[n]

result = min(v1_path,v2_path)

if result < inf:
    print(result)
else:
    print(-1)