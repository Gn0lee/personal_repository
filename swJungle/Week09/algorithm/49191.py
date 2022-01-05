from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    graph_reverse = defaultdict(list)
    
    for a, b in results:
        graph[a].append(b)
        graph_reverse[b].append(a)
        

    for i in range(1,n+1):
        visited = defaultdict(lambda : False)
        q = deque([i])
        visited[i] = True
        while q:
            now = q.popleft()     
            for j in graph[now]:
                if not visited[j]:
                    visited[j] = True
                    q.append(j)
        
        q = deque([i])      
        while q:
            now1 = q.popleft()
            for k in graph_reverse[now1]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)
                    
        if len(visited) == n:
            answer += 1
    
    return answer