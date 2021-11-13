import sys

from collections import deque
n , m = list(map(int,sys.stdin.readline().split()))
m_list = list(map(int,sys.stdin.readline().split()))
max_height = max(m_list)

def binary_search(arr,start,end,key):
    if start < end:
        return None
    mid = (start+end) //2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr,mid-1,end,key)
    else:
        return binary_search(arr,start,mid+1,key)


def sum_tree(h):
    ans = 0
    for i in m_list:
        if i > h:
            ans += (i-h)
    return ans

def binary_search_deque(start,end,key):
    
    q = deque()
    q.append([start,end])
    while q:
        cs , ce = q.popleft()
        mid = (cs+ce) //2
        if cs > ce:
            return mid
        if sum_tree(mid) == key:
            return mid
        elif sum_tree(mid) < key:
            q.append([cs,mid-1])
        else:
            q.append([mid+1,ce])
    

print(binary_search_deque(0,max_height,m))

