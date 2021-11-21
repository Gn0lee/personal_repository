import sys
from collections import deque
from heapq import heappush,heappop

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]
chk = [[False]*n for _ in range(n)]

for i in range(n):
    x = list(map(int,input().strip()))
    graph[i] = x

def bfs(y,x):

    q = []
    heappush(q,[0,y,x])
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while q:
        count , cy , cx = heappop(q)
        chk[cy][cx] = True
        if cy == n-1 and cx == n-1:
            return count

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if not chk[ny][nx]:
                    chk[ny][nx] = True
                    if graph[ny][nx] == 0:
                        heappush(q,[count+1,ny,nx])
                    else:
                        heappush(q,[count,ny,nx])


print(bfs(0,0))