from collections import deque
import sys
input = sys.stdin.readline

def find_miro(y,x):

    q = deque([])
    chk[y][x] = True
    ans[y][x] = 1
    q.append([y,x,1])

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while q:
        cy , cx , c = q.popleft()

        for i in range(4):
            ny , nx = cy +dy[i], cx +dx[i]
            if 0<=ny < n and 0<= nx < m:
                if not chk[ny][nx] and miro[ny][nx] == 1:
                    chk[ny][nx] = True
                    ans[ny][nx] = c+1
                    q.append([ny,nx,c+1])


n , m = map(int,input().split())
miro  = [list(map(int,input().strip())) for _ in range(n)]

chk = [[False]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]


find_miro(0,0)
print(ans[n-1][m-1])


