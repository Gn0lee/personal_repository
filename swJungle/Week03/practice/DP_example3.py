# N가지 종류의 화폐가 있다. 화폐를 최소한으로 사용하여 M원이 되도록 하려한다. 화폐 중복사용가능
# M원이 되기위한 최소한의 화폐 개수를 출력하시오
# N은 100 이하, M은 10000이하 조합이 불가능할 경우 -1출력


import sys
input = sys.stdin.readline

n,m = map(int,input().split())

money = []

for _ in range(n):
    money.append(int(input()))

dp = [10001] *(m+1)
dp[0] = 0
for i in money:
    for j in range(i,m+1):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j],dp[j-i]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])