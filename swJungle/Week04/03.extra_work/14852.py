def cal_tile(n):

    dp = [0] *(n+1)
    dp1 = [0] *(n+1)
    
    dp[0] = 1
    dp[1] = 2

    dp1[0] = 1
    dp1[1] = 3


    for i in range(2,n+1):
        dp[i] = (dp1[i-1] * 2) % 1000000007 + dp[i-2] % 1000000007
        dp1[i] = dp1[i-1] % 1000000007 + dp[i]% 1000000007

    return dp[n] % 1000000007




if __name__ == "__main__":
    n = int(input())

    if  n == 1:
        print(2)
        exit(0)
    elif n == 2:
        print(7)
        exit(0)
    else:
        print(cal_tile(n))