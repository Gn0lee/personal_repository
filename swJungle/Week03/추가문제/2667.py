import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]

chk = [[False]*n for _ in range(n)]

for i in range(n):
    x = list(map(int,input().strip()))
    graph[i] = x


result = []

def bfs(y,x):
    if graph[y][x] == 0 or chk[y][x] == True:
        return
    
    q= deque([])
    q.append([y,x])

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    chk[y][x] = True
    cnt = 1
    
    while q:
        cy , cx = q.popleft()

        for i in range(4):
            ny ,nx = cy + dy[i],cx+dx[i]

            if 0<=ny<n and 0<=nx<n and not chk[ny][nx] and graph[ny][nx] == 1:
                chk[ny][nx] = True
                cnt += 1
                q.append([ny,nx])

    result.append(cnt)


for j in range(n):
    for i in range(n):
        bfs(j,i)


result.sort()
print(len(result))
print(*result,sep="\n")

