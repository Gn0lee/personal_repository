import sys
input = sys.stdin.readline
inf = -int(1e9)
n = int(input())

nums = list(map(int,input().split()))

dp = [inf] * n
dp[0] = nums[0]

for i in range(1,n):
    dp[i] = max(nums[i],dp[i-1]+nums[i])

print(max(dp))
