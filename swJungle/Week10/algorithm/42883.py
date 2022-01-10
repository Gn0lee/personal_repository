from collections import deque

def solution(number, k):
    answer = ''
    number = deque(map(int,number))
    stack = []

    while number:
        now = number.popleft()
        
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
        for _ in range(k):
            stack.pop()
    
    answer = "".join(list(map(str,stack)))  
    return answer




print(solution("1000",2))
# print(solution("1231234",6))
# print(solution("4177252841",4))