import sys
input = sys.stdin.readline

def cal_time(time,n):
    time.sort()

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] , dp2[0] = time[0],time[0]

    for i in range(1,n):
        dp1[i] = time[i] + dp1[i-1]
        dp2[i] = dp1[i] + dp2[i-1]


    return dp2[n-1]





if __name__ == "__main__":
    n = int(input())
    time = list(map(int,input().split()))

    print(cal_time(time,n))