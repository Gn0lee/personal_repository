import sys
from bisect import bisect_right, bisect_left


liquid_num = int(input())
liquid_list = list(map(int,sys.stdin.readline().split()))
liquid_list.sort()

min_ph = 5000000000


if min(liquid_list) >= 0:
    ans_0 = 0
    ans_1 = 1
    
elif max(liquid_list) <= 0:
    ans_0 = -2
    ans_1 = -1
    
else: 
    if len(liquid_list) == 2:
        ans_0 = 0
        ans_1 = 1
        pass
    else:
        for i in range(liquid_num-1):
            start = i+1
            end = liquid_num-1
            
            while start <= end:
                mid = (start+end) //2
                a = liquid_list[i] + liquid_list[mid]    
                if abs(a) < min_ph:
                    min_ph = abs(a)
                    ans_0 = i
                    ans_1 = mid
                if a < 0:
                    start = mid + 1
                else:
                    end = mid - 1


print(liquid_list[ans_0],liquid_list[ans_1])

