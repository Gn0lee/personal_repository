from collections import deque

# a = "...!@BaT#*..y.abcdefghijklm"
# b = deque(map(str,a))
# print(b)



def solution(new_id):
    answer = ''
    #1단계
    answer += new_id.lower()

    tmp = deque(map(str,answer))
    #2단계
    for _ in range(len(tmp)):
        now = tmp.popleft()
        ascii_now = ord(now)
        if 97<=ascii_now<=122 or 48<=ascii_now<=57 or ascii_now == 45 or ascii_now == 95 or ascii_now == 46:
            tmp.append(now)
        else:
            continue
    
    #3단계
    stack = deque([tmp.popleft()])
    for _ in range(len(tmp)):
        now = tmp.popleft()
        if now == "." and stack[-1] == ".":
            continue
        else:
            stack.append(now)
    #4단계
    while stack:
        if stack[0] != "." and stack[-1] != ".":
            break
        elif stack[0] == ".":
            stack.popleft()
        else:
            stack.pop()

    #5단계
    if not stack:
        stack.append("a")
    
    #6단계
    while len(stack) >= 16:
        stack.pop()
    
    if stack[-1] == ".":
        stack.pop()
    
    #7단계
    while len(stack) <=2:
        stack += [stack[-1]]

    answer = "".join(list(stack))
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

