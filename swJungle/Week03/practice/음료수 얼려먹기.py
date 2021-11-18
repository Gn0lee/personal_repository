import sys
from collections import deque
from typing import AnyStr

n,m = map(int,sys.stdin.readline().split())

chk = [[False]*m for _ in range(n)]

ice = [list(map(int,sys.stdin.readline().split()))  for _ in range(n)  ]

dy = [-1,0,1,0]
dx = [0,-1,0,1]

global ans
ans = 0

def icecreem(y,x):

    q = deque([])
    q.append([y,x])

    while q:
        cy ,cx = q.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<= ny < n and 0<= nx < m :
                if not chk[ny][nx] and ice[ny][nx] == 0:
                    chk[ny][nx] = True
                    q.append([ny,nx])

cnt = 0

for j in range(n):
    for i in range(m):
        if ice[j][i] == 0 and not chk[j][i]:
            cnt += 1
            icecreem(j,i)


print(cnt)