from collections import deque
import sys
input = sys.stdin.readline

def bfs(y,x):
    if chk[y][x] or farm[y][x] ==0:
        return 0

    dy = [1,0,-1,0]
    dx = [0,-1,0,1]

    chk[y][x] = True
    q = deque([])
    q.append([y,x])

    while q:
        cy , cx = q.popleft()

        for i in range(4):
            ny , nx = cy + dy[i] , cx + dx[i]

            if 0<=ny<n and 0<=nx<m and not chk[ny][nx] and farm[ny][nx] == 1:
                chk[ny][nx] = True
                q.append([ny,nx])

    return 1


for _ in range(int(input())):

    m,n,k = map(int,input().split())
    farm = [[0]*m for _ in range(n)]
    chk = [[False]*m for _ in range(n)]
    result = 0

    for _ in range(k):
        a , b = map(int,input().split())
        farm[b][a] = 1


    for j in range(n):
        for i in range(m):
            result = result + bfs(j,i)

    print(result)
