import sys
from heapq import heappush,heappop
input = sys.stdin.readline

m , n ,h = map(int,input().split())

tomatos = [[[] for _ in range(n)] for x in range(h)]


for i in range(h):
    for j in range(n):
        x = list(map(int,input().split()))
        tomatos[i][j] = x

dy = [-1,0,1,0]
dx = [0,1,0,-1]
dh = [1,-1]

def bfs(y,x,h):
    
    q = []

    q.append([y,x,h])

    while q:
        cy , cx ,ch = heappop(q)

        for j in range(2):
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                nh = ch + dh[i]

                if 0<=nh<h and 0<=nx<m and 0<=ny<n and tomatos[nh][ny][nx] == 1:
                    heappush
