import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
global cnt
cnt = 0

def dfs(v):
    global cnt
    
    visited[v] = True

    for i in graph[v]:
        if not visited[i] and location[i] == 1:
            cnt += 1
            continue          
        elif not visited[i] and location[i] == 0:
            dfs(i)



n = int(input())

location = [0]+list(map(int,input().strip()))

graph = [[] for _ in range(n+1)]



for _ in range(n-1):
    a ,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    visited = [False] * (n+1)
    if not visited[i] and location[i] == 1:
        dfs(i)

print(cnt)