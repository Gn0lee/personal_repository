from functools import reduce
import sys
from collections import deque
input = sys.stdin.readline

m , n ,h = map(int,input().split())

tomatos = [[[0]*m for _ in range(n)] for x in range(h)]

q = deque([])
for i in range(h):
    for j in range(n):
        x = list(map(int,input().split()))
        for index,k in enumerate(x):
            if k == 1:
                q.append([i,j,index])
                tomatos[i][j][index] = k
            else:
                tomatos[i][j][index] = k

dy = [-1,0,1,0,0,0]
dx = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]


while q:
    ch,cy,cx = q.popleft()

    for i in range(6):
        ny = cy + dy[i]
        nx = cx + dx[i]
        nh = ch + dh[i]

        if 0<=nh<h and 0<=nx<m and 0<=ny<n and tomatos[nh][ny][nx] == 0:
            tomatos[nh][ny][nx] = tomatos[ch][cy][cx] + 1
            q.append([nh,ny,nx])

def time_cal():
    max_time = int(-1e9)
    for z in tomatos:
        for y in z:
            x = reduce(lambda a, b : a*b,y)
            if x == 0:
                return -1
            else:
                max_time = max(max_time,max(y))
    return max_time-1

print(time_cal())