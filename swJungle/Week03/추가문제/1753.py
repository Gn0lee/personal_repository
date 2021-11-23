import sys
from heapq import heappush,heappop
input = sys.stdin.readline

inf = int(1e9)

def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q,[0,start])

    while q:
        dist , now = heappop(q)

        if dist > distance[now]:
            continue

        for d,i in graph[now]:
            sum_dist = dist + d
            if sum_dist < distance[i]:
                distance[i] = sum_dist
                heappush(q,[sum_dist,i])


v,e = map(int,input().split())
start = int(input())

graph = [[] for _ in range(v+1)]

distance = [inf] * (v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])