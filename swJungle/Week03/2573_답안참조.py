import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from copy import deepcopy
from functools import reduce
from collections import deque

def dfs(y,x):

    if 0<=y<n and 0<= x <m and chk[y][x] >0 :
        chk[y][x] = 0
        
        dfs(y+1,x)
        
        dfs(y-1,x)
        
        dfs(y,x+1)
        
        dfs(y,x-1)

        return True
    
    else:
        return False


n , m = map(int,input().split())

icebergs = [[] for _ in range(n)]

q= deque([])

for j in range(n):
    x = list(map(int,input().split()))
    icebergs[j] = x
    for i , k in enumerate(x):
        if k != 0:
            q.append((j,i))

year = 0 

dy = [-1,0,1,0]
dx = [0,1,0,-1]




while q:
    
    if len(q) <= 1:
        print(0)
        exit(0)

    chk = deepcopy(icebergs)
    start_y ,start_x = q[0]
    dfs(start_y,start_x)

    for X in chk:
        a = reduce(lambda x,y : x+y,X)
        if a != 0:
            print(year)
            exit(0)
    
    
    chk1 = [[False]*m for _ in range(n)]
    
    for _ in range(len(q)):
        
        cy,cx = q.popleft()
        
        for i in range(4):
        
            ny,nx = cy + dy[i],cx+dx[i]
            
            if 0<=ny<n and 0<=nx<m and icebergs[ny][nx] == 0 and not chk1[ny][nx]:
                icebergs[cy][cx] -= 1
        chk1[cy][cx] = True
        
        if icebergs[cy][cx] <=0:
            icebergs[cy][cx] = 0

        else:
            q.append([cy,cx])
            
    year +=1
        
# print(0)