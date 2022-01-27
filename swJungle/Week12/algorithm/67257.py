from itertools import permutations
from collections import deque

def solution(expression):
    answer = -1
    exp_list = []
    tmp = ""
    operators = set()
    
    for c in expression:
        if c == "*" or c == "+" or c == "-":
            exp_list.append(int(tmp))
            exp_list.append(c)
            operators.add(c)
            tmp = ""
        else:
            tmp += c
    exp_list.append(int(tmp))
    # print(exp_list)
    
    for operators_set in permutations(list(operators),len(operators)):
        q = deque(exp_list)
        stack = []
        for operator in operators_set:
            for _ in range(len(q)):
                now = q.popleft()
                if q[-1] == operator:
                    q.pop()
                    x = q.pop()
                    if operator == "*":
                        q.append(x*now)
                    elif operator == "+":
                        q.append(x+now)
                    else:
                        q.append(x-now)
                else:
                    q.append(now)
        answer = max(answer, abs(q.pop()))
                    
    
    return answer