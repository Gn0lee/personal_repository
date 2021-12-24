from heapq import _heapify_max, heapify, heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
inf = int(1e9)
inf_min = -int(1e9)
def solution(operations):
    # answer = []
    # q_max = []
    # q_min = []
    # chk = [False] * 1000001
    # operations = deque(operations)
    # while operations:
    #     now_operand, now_num = operations.popleft().split()
    #     now_num = int(now_num)
    #     if now_operand == "I":
    #         heappush(q_min,now_num)
    #         heappush(q_max,-now_num)
    #         chk[now_num] = False
    #     elif q_max and not chk[now_num] and now_num == 1:
    #         heappop(q_max)
    #         chk[now_num] = True
    #     elif q_min and not chk[now_num] and now_num == -1:
    #         heappop(q_min)
    #         chk[now_num] = True
    #     else:
    #         continue
    # max_val , min_val = inf_min , inf
    # while q_max:
    #     now = -heappop(q_max)
    #     if not chk[now]:
    #         max_val = max(max_val,now)
    #         break

    # while q_min:
    #     now = heappop(q_min)
    #     if not chk[now]:
    #         min_val = min(min_val,now)
    #         break

    # if max_val == inf_min and min_val == inf:
    #     print("EMPTY") 
    # elif max_val == inf_min:
    #     print("{} {}".format(min_val,min_val))
    # elif min_val == inf:
    #     print("{} {}".format(max_val,max_val))
    # else:
    #     print("{} {}".format(max_val,min_val))
    min_heap = []
    max_heap = []
    heap_cnt = 0
    for oper in operations :
        # 문자와 숫자 split
        order, num = oper.split(' ')
        if order == "I" :
            heappush(min_heap, int(num))
            heappush(max_heap, -int(num))
            heap_cnt += 1
        elif order == "D" :
            if heap_cnt > 0 :
                if num == "-1" :
                    heappop(min_heap)
                elif num == "1" :
                    heappop(max_heap)
                heap_cnt -= 1
                # 힙 카운트 0이 되면 한 번은 pop이 되었던 숫자들만 남음
                # 최대 최소 힙을 비움 list.clear()
                if heap_cnt == 0 :
                    min_heap.clear()
                    max_heap.clear()
                    
    if heap_cnt > 0 :
        # answer = [-heappop(max_heap), heappop(min_heap)]
        print(-heappop(max_heap), heappop(min_heap))
    else :
        # answer = [0, 0]
        print("EMPTY")

# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

if __name__ == "__main__":
    for _ in range(int(input())):
        problem = []
        for __ in range(int(input())):
            problem.append(input().strip())
        solution(problem)
       
        