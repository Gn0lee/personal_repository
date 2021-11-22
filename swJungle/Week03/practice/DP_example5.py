#병사 배치하기

import sys
input = sys.stdin.readline

n = int(input())

soldiers = list(map(int,input().split()))

soldiers.reverse()

dp = [1]*n #자기자신 1개도 수열 1개이므로 1로 초기화

for i in range(1,n):
    for j in range(0,i):
        if soldiers[j] < soldiers[i]: #i번째 수열의 값이 j번째 수열의 값보다 클때(증가할때)
            dp[i] = max(dp[i],dp[j]+1) #j번째 에서 하나 더한값과 i자체값 중 더 큰값으로 갱신

print(n-max(dp)) #열외시키는 병사의 수를 계산