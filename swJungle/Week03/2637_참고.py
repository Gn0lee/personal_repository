import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
graph2 = [[0]*(N+1) for _ in range(N+1)]
counts = [0]*(N+1)

for _ in range(M):
    a , b, c = map(int,input().split())
    graph[b].append([a,c])
    counts[a] = counts[a] + 1

def cal_parts():
    q= deque([])
    # basic = 0
    for i in range(1,N+1):
        if counts[i] == 0:
            q.append(i)
            # basic += 1

    while q:
        now = q.popleft()
        if graph2[now].count(0) == N+1:
            for i in graph[now]:
                counts[i[0]] -= 1
                graph2[i[0]][now] += i[1]
                if counts[i[0]] == 0:
                    q.append(i[0])
        else:
            for i in graph[now]:
                counts[i[0]] -= 1
                for j in range(1,N+1):
                    graph2[i[0]][j] += graph2[now][j] * i[1]
                if counts[i[0]] == 0:
                    q.append(i[0])

    return


num_basic = cal_parts()
# print(*graph2,sep="\n")

for x in range(1,N+1):
    if graph2[N][x] !=0:
        print(x,graph2[N][x],sep=" ")