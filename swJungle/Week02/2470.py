import sys
from bisect import bisect_right, bisect_left


liquid_num = int(input())
liquid_list = list(map(int,sys.stdin.readline().split()))
liquid_list.sort()

min_ph = 5000000000
min_liquid_pair = [0,0]

if min(liquid_list) >= 0:
    min_liquid_pair[0] = liquid_list[0]
    min_liquid_pair[1] = liquid_list[1]
    
elif max(liquid_list) <= 0:
    min_liquid_pair[0] = liquid_list[-2]
    min_liquid_pair[1] = liquid_list[-1]
    
else:    
    end_point_index = bisect_left(liquid_list,0)-1    
            
    for i in range(0,end_point_index+1):
        if -liquid_list[i] in liquid_list:
            min_liquid_pair[0] = liquid_list[i]
            min_liquid_pair[1] = -liquid_list[i]
            break
        else:
            pair_liquid_index = bisect_left(liquid_list,-liquid_list[i])-1
            pH_mix = liquid_list[i]+liquid_list[pair_liquid_index]
            if abs(pH_mix) < min_ph:
                min_ph = abs(pH_mix)
                min_liquid_pair[0] = liquid_list[i]
                min_liquid_pair[1] = liquid_list[pair_liquid_index]
    if 0 in liquid_list:
        zero_index = bisect_left(liquid_list,0)
        if -liquid_list[zero_index-1] < min_ph:
            min_liquid_pair[0] = liquid_list[zero_index-1]
            min_liquid_pair[1] = liquid_list[zero_index]
        if liquid_list[zero_index+1] < min_ph:
            min_liquid_pair[0] = liquid_list[zero_index]
            min_liquid_pair[1] = liquid_list[zero_index+1]

print(min_liquid_pair[0],min_liquid_pair[1])

