import sys
input = sys.stdin.readline

inf = int(2**31)

n = int(input())

dp = [[inf]*(n+1) for _ in range(n+1)]

for x in range(1,n+1):
    dp[x][x] = 0

p_list = [0] * (n+1)

for i in range(n):
    a , b = map(int,input().split())
    p_list[i] = a
    p_list[i+1] = b

for j in range(1,n+1):
    for i in range(j-1,0,-1):
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+p_list[i-1]*p_list[k]*p_list[j])

print(dp[1][n])