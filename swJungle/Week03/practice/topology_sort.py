from collections import deque

def topology_sort():
    q = deque([])

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]: #현재 노드에서 진입하는 간선 제거
            indegree[i] -= 1
            
            if indegree[i] == 0: #진입차수가 0인 노드를 q에 삽입
                q.append(i)


result = []
v , e = map(int,input().split())

indegree = [0] *(v+1) ##노드로 들어오는 수를 셈
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a , b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1 #b로 들어오는 것이므로 인덱스 b의 값을 1증가시켜줌.