from collections import defaultdict,deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    chk = defaultdict(lambda : False)
    answer_dict = defaultdict(lambda : 0)
    
    for start , end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    def bfs():
        q = deque([1])
        chk[1] = True
        level = 0

        while q:
            
            for _ in range(len(q)):
                now = q.popleft()
                answer_dict[level] += 1
                for next_node in graph[now]:
                    if not chk[next_node]:
                        q.append(next_node)
                        chk[next_node] = True
            level += 1            
        
        return level-1
            
    answer = answer_dict[bfs()]    
           
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])