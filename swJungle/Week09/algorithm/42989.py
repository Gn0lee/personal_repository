def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    
    inf = int(1e9)
    dp[0][0] = 1

    for x , y in puddles:
        dp[y-1][x-1] = inf

    for k in range(1,m+n-1):
        for j in range(k+1):
            i = k - j
            if 0<=j<n and 0<=i<m:
                if dp[j][i] == inf:
                    continue
                elif j == 0:
                    dp[j][i] = dp[j][i-1]
                elif i == 0:
                    dp[j][i] = dp[j-1][i]
                else:
                    if dp[j-1][i] != inf and dp[j][i-1] != inf:
                        dp[j][i] = dp[j-1][i]%1000000007 + dp[j][i-1]%1000000007
                    elif dp[j-1][i] == inf:
                        dp[j][i] = dp[j][i-1]
                    else:
                        dp[j][i] = dp[j-1][i]

    answer = dp[n-1][m-1]%1000000007
    if answer == inf:
        answer = 0    
    return answer


print(solution(4,3,[[1,2],[2,1]]))