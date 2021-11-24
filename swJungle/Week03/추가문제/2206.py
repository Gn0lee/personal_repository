
import sys
from collections import deque
input =  sys.stdin.readline

def bfs(y,x):

    q = deque([])
    chk[0][y][x] = 1

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    q.append([0,y,x])

    while q:
        z, cy , cx = q.popleft()

        if cy == n-1 and cx == m-1:
            return chk[z][cy][cx]
        
        for i in range(4):

            ny , nx = cy + dy[i],cx+dx[i]

            if z == 0:
                if 0<=ny<n and 0<=nx<m:
                    if chk[z][ny][nx] == 0:
                        if graph[ny][nx] == 0:
                            chk[z][ny][nx] = chk[z][cy][cx] + 1
                            q.append([z,ny,nx])
                        elif graph[ny][nx] == 1:    
                            chk[z+1][ny][nx] = chk[z][cy][cx] + 1
                            q.append([z+1,ny,nx])
            else:
                if 0<=ny<n and 0<=nx<m:
                    if chk[z][ny][nx] == 0 and graph[ny][nx] == 0:
                        chk[z][ny][nx] = chk[z][cy][cx] + 1
                        q.append([z,ny,nx])

    return -1

    

n , m = map(int,input().split())


graph = [[] for _ in range(n)]

chk = [[[0]*m for _ in range(n)] for __ in range(2)]

for i in range(n):
    x = list(map(int,input().strip()))
    graph[i] = x

if n == 1 and m == 1 and graph[0][0] == 0:
    print(1)
    exit(0)


print(bfs(0,0))

