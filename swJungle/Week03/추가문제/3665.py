import sys
input  = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n = int(input())
    rank_list = list(map(int,input().split()))
    m = int(input())

    graph = [[] for a in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n-1):
        for j in range(i+1,n):
            graph[rank_list[i]].append(rank_list[j])
            indegree[rank_list[j]] += 1

    for k in range(m):
        a , b = map(int,input().split())
        chk = True
        for x in graph[a]:
            if x == b:
                graph[a].remove(b)
                indegree[a] += 1
                graph[b].append(a)
                indegree[b] -= 1
                chk = False
        if chk:
            graph[b].remove(a)
            indegree[b] += 1
            graph[a].append(b)
            indegree[a] -= 1

    q = deque([])
    for l in range(1,n+1):
        if indegree[l] == 0:
            q.append(l)
    
    chk1 = True
    result = []
    if not q:
        chk1 = False

    while q:
        if len(q) >1:
            chk1 = False
            break
        now = q.popleft()
        result.append(now)
        for z in graph[now]:
            indegree[z] -= 1
            if indegree[z] <0:
                chk1 = False
                break
            elif indegree[z] == 0:
                q.append(z)

    if not chk1 or len(result) < n:
        print("IMPOSSIBLE")
    else:
        print(*result)
