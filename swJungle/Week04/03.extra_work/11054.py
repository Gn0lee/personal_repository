import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))

def cal_lis(arr):

    x = len(arr)
    dp_lis = [1] * x

    for i in range(1,x):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_lis[i] = max(dp_lis[i],dp_lis[j]+1)

    return dp_lis[x-1]


def cal_rev_lis(arr):
    x = len(arr)
    dp_lis = [1] * x
    arr.reverse()
    for i in range(1,x):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_lis[i] = max(dp_lis[i],dp_lis[j]+1)

    return dp_lis[x-1]

dp_bitonic = [1] * n

for k in range(n):
    a = cal_lis(nums[:k+1])
    b = cal_rev_lis(nums[k:])

    dp_bitonic[k] = a + b -1

print(max(dp_bitonic))
