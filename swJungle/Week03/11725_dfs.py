import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

n = int(input())
parent = [0]*(n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a , b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)    


def dfs(v,parent):

    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i,parent)

def bfs(v,parent):

    q = deque([])
    q.append(v)
    while q:
        now = q.popleft()

        for i in graph[now]:
            if parent[i] == 0:
                parent[i] = now
                q.append(i)


bfs(1,parent)
print(*parent[2:],sep="\n")