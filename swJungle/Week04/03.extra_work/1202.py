import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def cal_val(gems,bags):

    result = 0
    tmp = []

    for _ in range(len(bags)):
        capacity = heappop(bags)
        
        while gems and gems[0][0] <= capacity:
            _ , value = heappop(gems)
            heappush(tmp,-value)

        if tmp:
            result += -heappop(tmp)
        elif not gems:
            break        
        
    return result



if __name__ == "__main__":
    n, m = map(int,input().split())
    gems = []
    bags = []

    for _ in range(n): 
        w, v = map(int,input().split())
        heappush(gems,[w,v])
                     
    for __ in range(m):
        heappush(bags,int(input()))

    print(cal_val(gems,bags))