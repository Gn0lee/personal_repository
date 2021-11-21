from heapq import heappop,heappush
import sys
input = sys.stdin.readline

INF = int(1e9)

n , m = map(int,input().split())

start = int(input())
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a , b, c = map(int,input().split())

    graph[a].append((c,b))

def dijkstra_heap(start):
    q = []
    distance[start] = 0
    heappush(q,(0,start))

    while q:
        dist , now = heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heappush(q,(cost,i[1]))

dijkstra_heap(start)
