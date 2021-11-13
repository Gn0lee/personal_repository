from collections import deque
import sys
import heapq


liquid_num = int(input())
liquid_list = list(map(int,sys.stdin.readline().split()))
ans_list = [0]
character_num = 3000000000
heapq._heapify_max(liquid_list)
if liquid_list[0] < 0:
    a = liquid_list.pop(0)
    heapq._heapify_max(liquid_list)
    b = liquid_list.pop(0)
    del ans_list[0]
    ans_list.append([b,a])
else:
    heapq.heapify(liquid_list)

    if liquid_list[0] > 0:
        a = heapq.heappop(liquid_list)
        heapq.heapify(liquid_list)
        b = heapq.heappop(liquid_list)
        del ans_list[0]
        ans_list.append([a,b])
    else:
        while len(liquid_list) > 1:
            heapq.heapify(liquid_list)
            a = heapq.heappop(liquid_list)
            heapq._heapify_max(liquid_list)
            b = heapq.heappop(liquid_list)
            if a + b < character_num:
                character_num = a+b
                del ans_list[0]
                ans_list.append([a,b])

a , b = ans_list[0]
print(a,b)


