import sys
input = sys.stdin.readline
from heapq import heappop,heappush


def topology_sort():
    q = []
    for i in range(1,n+1):
        if outdegree[i] == 0:
            heappush(q,-i)
    N = n
    while q:
        now = -heappop(q)
        result[now] = N
        for k in graph[now]:
            outdegree[k] -= 1
            if outdegree[k] == 0:
                heappush(q,-k)

        N -= 1


n = int(input())

outdegree = [0]*(n+1)

result = [0]*(n+1)

graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    x = list(map(int,input().strip()))
    for j,k in enumerate(x):
        if k==1:
            graph[j+1].append(i)
            outdegree[i] +=1


topology_sort()

if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])


