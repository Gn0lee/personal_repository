import copy
import sys
from collections import deque

n = int(input())
num_list = list(map(int,sys.stdin.readline().split()))
sort_list = list()
global ans
ans = 0


def swap(arr):
    global ans
    beforeswap = list(map(lambda x : x , arr))
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1],arr[i]
            ans += 1
    print(arr)
    if beforeswap == arr:
        return
    else: 
        swap(arr)
    
            
        
            

        

# swap(num_list)
print(ans)