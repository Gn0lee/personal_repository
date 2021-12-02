import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)



def dfs(y,x):
    if y == m-1 and x == n-1:
        return 1
    if dp[y][x] == -1:
        return 0

    if dp[y][x]:
        return dp[y][x]

    cnt = 0

    if 0<=y+1<m and 0<=x<n and graph[y][x] > graph[y+1][x]:
        cnt += dfs(y+1,x)
    if 0<=y<m and 0<=x+1<n and graph[y][x] > graph[y][x+1]:
        cnt += dfs(y,x+1)
    if 0<=y-1<m and 0<=x<n and graph[y][x] > graph[y-1][x]:
        cnt += dfs(y-1,x)
    if 0<=y<m and 0<=x-1<n and graph[y][x] > graph[y][x-1]:
        cnt += dfs(y,x-1)

    if cnt == 0:
        dp[y][x] = -1
        return 0 
    
    dp[y][x] = cnt

    return dp[y][x]

if __name__ == "__main__":
    m , n = map(int,input().split())

    graph = [list(map(int,input().split())) for _ in range(m)]

    dp = [[0]*n for _ in range(m)]

    ans = dfs(0,0)
    print(ans)
    # print(dp) 