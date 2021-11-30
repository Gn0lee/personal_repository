import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

stair = [0]

for _ in range(n):
    stair.append(int(input()))

dp[1] = stair[1]

if n == 1:
    print(dp[1])
    exit(0)

dp[2] = stair[1] + stair[2]

if n == 2:
    print(dp[2])
    exit(0)

for i in range(3,n+1):
    dp[i] = max(dp[i-2],dp[i-3] + stair[i-1]) +stair[i] 

print(dp[n])
