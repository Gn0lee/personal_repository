def solution(priorities, location):
    from collections import deque
    answer = 0
    priorities = deque(priorities)
    index_list = deque([])
    
    for i in range(len(priorities)):
        index_list.append(i)
    
    answer_list = [0] * 100
    
    count = 1
    while priorities:
        now_p , now_i = priorities.popleft() , index_list.popleft()
        
        if priorities and now_p < max(priorities):
            priorities.append(now_p)
            index_list.append(now_i)
        elif priorities and now_p >= max(priorities):
            answer_list[now_i] = count
            count += 1
        else:
            answer_list[now_i] = count
    
    answer = answer_list[location]
    
    return answer

print(solution([2,1,3,2],2))