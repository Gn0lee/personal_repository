from collections import deque

def solution(number, k):
    answer = ''
    stack = []

    for now in number:
        
        while True:
            if not stack or k == 0:
                stack.append(now)
                break
            elif stack[-1] < now:
                stack.pop()
                k -= 1
            else:
                stack.append(now)
                break

    if k >0:
        stack = stack[:-k]
    
    answer = "".join(stack)  
    return answer





print(solution("1000",2))
# print(solution("1231234",6))
# print(solution("4177252841",4))