import sys
input = sys.stdin.readline
INF = int(1e9)

n , m = map(int,input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

visited = [False]*(n+1)

distance = [INF] *(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) #그래프에 a->b로 가는 비용 c를 저장

def get_smallest_node(): #아직 방문하지 않은 노드 중 거리가 최소인 곳의 인덱스를 반환
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):

    distance[start] = 0
    visited[start] = True

    #start와 인접한 노드들의 거리초기화 (INF -> c)
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    #시작노드를 제외한 노들에 대하여 반복작업
    for i in range(n-1):
        now = get_smallest_node() #아직 방문하지 않은곳 중 거리가 가장짧은곳의 인덱스
        visited[now] = True #선정된 가장 가까운곳 방문처리
        for j in graph[now]: #선정된 노드와 인접한 노들들에 대해서 최소거리 갱신
            cost = j[1] + distance[now]
            if cost < distance[j[1]]: #시작노드에서 인접 노드로 가는 거리와 선정된 노드를 거쳐서 인접노드로 가는 거리를 비교하여 최소거리 갱신 
                distance[j[1]] = cost

dijkstra(start)
