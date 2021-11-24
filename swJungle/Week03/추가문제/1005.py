from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,k = map(int,input().split())
    build_time = [0]+list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    
    result = [0]*(n+1)
    indegree = [0]*(n+1)
    

    for _ in range(k):
        a , b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1 

    q = deque([])
    w = int(input())

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = build_time[i]

    while q:
        now = q.popleft()
        
        for j in graph[now]:
            result[j] = max(result[j],result[now]+build_time[j])
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

    print(result[w])