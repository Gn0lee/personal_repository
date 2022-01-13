from collections import deque

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[0])
    stack = []
    routes = deque(routes)
    while routes:
        start , end = routes.popleft()
        
        if not stack:
            stack.append([start, end])
        elif start <= stack[-1][1]:
            stack[-1][0] = start
            stack[-1][1] = min(end,stack[-1][1])
        else:
            stack.append([start,end])
            
    answer = len(stack)
        
    return answer

print(solution([[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]))