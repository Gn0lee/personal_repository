import sys
from collections import deque
input = sys.stdin.readline


n , k = map(int,input().split())
graph = [[] for _ in range(n)]

q = deque([])

for i in range(n):
    graph[i] = list(map(int,input().split()))
    for index , j in enumerate(graph[i]):
        if j !=0:
            q.append([j,i,index])

s , target_y,target_x = map(int,input().split())

dy = [-1,0,1,0]
dx = [0,1,0,-1]

count = 0

while count<s:
    q = deque(sorted(list(q)))
    for _ in range(len(q)):
        virus,cy , cx = q.popleft()
        
        for k in range(4):
            ny , nx = cy+dy[k], cx + dx[k]
            if 0<=ny<n and 0<=nx<n and graph[ny][nx] == 0:
                graph[ny][nx] = virus
                q.append([virus,ny,nx])
    count += 1

target_status = graph[target_y-1][target_x-1]
# print(graph)
print(target_status)