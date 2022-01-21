from collections import deque,Counter

def chk_balance(p):
    p = Counter(p)

    if p["("] == p[")"]:
        return True
    else:
        return False 
    
def chk_right(p):
    stack = []
    p = deque(p)
    
    while p:
        now = p.popleft()
        if not stack:
            stack.append(now)
        elif stack[-1] == "(" and now == ")":
            stack.pop()
        else:
            stack.append(now)
    if not stack:
        return True
    else:
        return False

def reverse_str(p):
    stack = []
    p = deque(p)

    p.popleft()
    p.pop()

    while p:
        now = p.popleft()
        if now == "(":
            stack.append(")")
        else:
            stack.append("(")

    return "".join(stack)

def edit_str(s):
    if len(s) == 0:
        return s
    u, v = s[:1],s[1:]
    for i in range(0,len(s)):
        if chk_balance(s[:i+1]) and chk_balance(s[i+1:]):
            u, v = s[:i+1],s[i+1:]
            break
    
    if chk_right(u):
        return u + edit_str(v)
    else:
        a = "(" + edit_str(v) + ")"
        return a + reverse_str(u)

def solution(p):
    
    if chk_right(p):
        answer =  p
    else:
        answer = edit_str(p)

    return answer


# a = "(()))("
# b = a[:2]
# a = a.lstrip("(")
# print(b)
# print(a)

# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))
print(solution("))()(("))
# s = ")("
# print(s[:2])
# print(edit_str(s))