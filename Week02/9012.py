import sys

t = int(input())

for _ in range(t):
    
    vps_list = list(sys.stdin.readline().strip())
        
    while vps_list:
        if vps_list[0] == ")" or vps_list[-1] == "(" :
            stack = []
            break
        stack = []
        stack.append(vps_list.pop(0))
        while stack:
            if len(vps_list) == 0:
                break
            elif vps_list[0] == stack[-1]:
                stack.append(vps_list.pop(0))
            else:
                del vps_list[0]
                del stack[-1]   
    if len(stack) != 0 or len(vps_list) != 0:
        print("NO")
        continue
    else:
        print("YES")

