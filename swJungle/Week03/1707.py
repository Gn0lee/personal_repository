from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(v):
    visited[v] = 1
    q = deque([])
    q.append(v)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] *(-1)
                q.append(i)
            elif visited[i] == visited[now]:
                return False

    return True

def dfs(v,group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i,-group):
                return False
        elif visited[i] == visited[v]:
            return False
    return True


k = int(input())
for _ in range(k):
    v ,e = map(int,input().split())
    visited = [0] *(v+1)
    graph = [[] for _ in range(v+1)]
    chk = True
    for _ in range(e):
        a , b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for x in range(1,v+1):
        if visited[x] == 0:
            if not bfs(x):
                chk = False
                break

    if chk:
        print("YES")
    else:
        print("NO")