import sys
input  = sys.stdin.readline

n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
operators = list(map(int,sys.stdin.readline().split())) # +, - ,X ,%


global maximum,minimum
maximum = -1e9
minimum = 1e9


def dfs(level,total,plus,minus,multi,divide):
    global maximum,minimum
    
    if level == n:
        maximum = max(maximum,total)
        minimum = min(minimum,total)
        return
    if plus:
        dfs(level+1,total+nums[level],plus-1,minus,multi,divide)
    if minus:
        dfs(level+1,total-nums[level],plus,minus-1,multi,divide)
    if multi:
        dfs(level+1,total*nums[level],plus,minus,multi-1,divide)
    if divide:
        dfs(level+1,int(total/nums[level]),plus,minus,multi,divide-1)

dfs(1,nums[0],operators[0],operators[1],operators[2],operators[3])
print(maximum)
print(minimum)
