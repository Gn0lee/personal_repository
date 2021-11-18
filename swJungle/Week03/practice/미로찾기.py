import sys
from collections import deque
from typing import AnyStr

n,m = map(int,sys.stdin.readline().split())

chk = [[False]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]

miro = [list(map(int,sys.stdin.readline().split()))  for _ in range(n)  ]

dy = [-1,0,1,0]
dx = [0,1,0,-1]



def icecreem(y,x):
  
    q = deque([])
    q.append([y,x,1])
    ans[y][x] = 1
    chk[y][x] = True
    while q:
        cy ,cx,node = q.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<= ny < n and 0<= nx < m :
                if not chk[ny][nx] and miro[ny][nx] == 1:
                    chk[ny][nx] = True
                    ans[ny][nx] = node + 1
                    
                    
                    q.append([ny,nx,node+1])

cnt = 10000000000


icecreem(0,0)


print(ans[n-1][m-1])