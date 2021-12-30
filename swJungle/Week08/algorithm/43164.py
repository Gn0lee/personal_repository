from collections import defaultdict, deque


def solution(tickets):
    
    answer = deque([])
    graph = defaultdict(list)
    
    for ticket in tickets:
        depart, arrival = ticket        
        graph[depart].append(arrival)
    
    for i in graph.values():
        i.sort()
    
    
    def dfs ():
        
        stack = ["ICN"]
        while len(stack) > 0 :

            now = stack[-1]

            if now not in graph or len(graph[now]) == 0:
                answer.appendleft(stack.pop())
            else:
                stack.append(graph[now].pop(0))
    
    dfs()
    answer = list(answer)
    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))