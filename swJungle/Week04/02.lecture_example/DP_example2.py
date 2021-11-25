# X가 5로 나누어 떨어지면 5로 나누기, 3으로 나누어 떨어지면 3으로 나누기, 2로 나누어 떨어지면 2로 나누기 , 1빼기 중 하나를 수행
# X가 1이 될때까지 최소한의 연산을 수행하고자 할때, 연산 수행 회수를 구하시오.
# X는 3만 이하


import sys
input = sys.stdin.readline

x = int(input())

dp = [0] *30001



for i in range(2,x+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%5 == 0:
        dp[i] = min(dp[i],dp[i//5]+1)

print(dp[x])