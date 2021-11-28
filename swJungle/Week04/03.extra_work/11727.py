def cal_tile(n):
    if n ==1:
        print(1)
        exit(0)
    
    dp = [0] *(n+1)

    dp[1] = 1
    dp[2] = 3

    for i in range(3,n+1):
        dp[i] = dp[i-1]%10007 + (2*dp[i-2])%10007

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(cal_tile(n)%10007)