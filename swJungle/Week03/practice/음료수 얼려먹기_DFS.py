import sys
from collections import deque
from typing import AnyStr

n,m = map(int,sys.stdin.readline().split())

chk = [[False]*m for _ in range(n)]

ice = [list(map(int,sys.stdin.readline().split()))  for _ in range(n)  ]

dy = [-1,0,1,0]
dx = [0,-1,0,1]


def DFS(y,x):

    if y<0 or y >=n or x <0 or x >=m:   
        
        return False
    
    if ice[y][x] == 0:
        
        ice[y][x] = 1
        
        DFS(y-1,x)
        DFS(y+1,x)
        DFS(y,x-1)
        DFS(y,x+1)
        
        return True
    return False



cnt = 0

for j in range(n):
    for i in range(m):
        if DFS(j,i):
            cnt += 1


print(cnt)