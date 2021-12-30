# 뭔가 풀긴 풀었으니 찝찝..
# 내리막길 문제처럼 경로의 수를 세야하는데 떠오르질 않음
# global 변수 안쓰고 푸는법 아시는분..?

global z
z = 0

def solution(numbers, target):
    global z
    
    def dfs(y,x,i,n,t):
        global z
        if i > n:
            if y - x == t:
                z += 1
            return
        dfs(numbers[i]+y,x,i+1,n,t)
        dfs(y,x+numbers[i],i+1,n,t)
        
    dfs(0,0,0,len(numbers)-1,target)    
    
    return z

print(solution([1, 1, 1, 1, 1],3))