import sys
input = sys.stdin.readline

dp = [0] * 101

dp[1],dp[2],dp[3],dp[4],dp[5],dp[6],dp[7],dp[8] = 1,1,1,2,2,3,4,5

for i in range(9,101):
    dp[i] = dp[i-1] + dp[i-5]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])