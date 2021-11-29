import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * n
dp_idx = [0] * n

rgb_list = []

for _ in range(n):
    a ,b,c = map(int,input().split())
    rgb_list.append([a,b,c])

dp = [[0]*3 for _ in range(n)]

dp[0][0] , dp[0][1] , dp[0][2] = rgb_list[0][0], rgb_list[0][1] , rgb_list[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb_list[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb_list[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + rgb_list[i][2]


print(min(dp[n-1]))