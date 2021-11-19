from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    q = deque([])

    for i in range(1,v+1):
        if chk[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for j in graph[now]:
            chk[j] -= 1
            if chk[j] == 0:
                q.append(j)




result = []
v , e = map(int,input().split())
chk = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a , b = map(int,input().split())
    graph[a].append(b)
    chk[b] += 1

topology_sort()

print(*result)