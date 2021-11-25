# 첫재 줄에 식량창고의 개수 N이 주어진다.(100이하)
# 둘째줄에 공백을 기준으로 각 식량창고에 저장된 식량의 개수 K가 주어진다(1000이하)
# 개미전사는 인접한 창고를 약탈하지 못할때 개미전사가 얻을수 있는 식량의 최대값을 출력하시오


import sys
input = sys.stdin.readline

n = int(input())
warehouse = list(map(int,input().split()))

dp = [0] * 100

dp[0] = warehouse[0]
dp[1] = max(warehouse[0],warehouse[1])

for i in range(2,n):
    dp[i] = max(dp[i-2]+warehouse[i],dp[i-1])

print(dp)