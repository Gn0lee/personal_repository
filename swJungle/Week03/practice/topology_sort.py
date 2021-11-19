from collections import deque

def topology_sort():
    q = deque([])

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)


result = []
v , e = map(int,input().split())

indegree = [0] *(v+1) ##노드로 들어오는 수를 셈
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a , b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1 #b로 들어오는 것이므로 인덱스 b의 값을 1증가시켜줌.