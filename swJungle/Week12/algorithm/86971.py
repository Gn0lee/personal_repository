from collections import defaultdict,deque
from itertools import combinations

def solution(n, wires):
    answer = 1000
    graph = defaultdict(list)
    
    for s,e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    for a , b in wires:
        q = deque([a])
        visited = defaultdict(lambda : False)
        visited[a] = True
        visited[b] = True
        
        num_a = 1   
        while q:
            now = q.popleft()
            for n in graph[now]:
                if n != b and not visited[n]:
                    visited[n] = True
                    num_a += 1
                    q.append(n)
        
        q = deque([b])
        num_b = 1   
        while q:
            now = q.popleft()
            for k in graph[now]:
                if k != a and not visited[k]:
                    visited[k] = True
                    num_b += 1
                    q.append(k)
        
        answer = min(answer,abs(num_a-num_b))
                      
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))