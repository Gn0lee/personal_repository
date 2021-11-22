import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
counts = [0]*(N+1)
result = [0]*(N+1)
for _ in range(M):
    a , b, c = map(int,input().split())
    graph[b].append(a)
    graph2[a].append([b,c])
    counts[a] = counts[a] + 1

def cal_parts():
    q= deque([])
    basic = 0
    for i in range(1,N+1):
        if counts[i] == 0:
            q.append(i)
            basic += 1

    while q:
        now = q.popleft()

        for i in graph[now]:
            counts[i] = counts[i] - 1
            for j in graph2[i]:
                if j[0] == now and j[0] > basic:
                    result[j[0]] = result[j[0]] +j[1]
            if counts[i] == 0:
                q.append(i)
    return basic


num_basic = cal_parts()
print(result)

for i in range(N,num_basic,-1):
    for j in graph2[i]:
        # if j[0] <= num_basic:
        result[j[0]] = result[j[0]] + j[1] * result[i]

print(result)