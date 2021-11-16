from collections import deque
import sys

def searchTower(arr,n):
    result = [0] * n
    stack = []
    for i in range(n-1,-1,-1):
        stack.append([i,arr.pop()])
        while stack and arr and arr[-1] >= stack[-1][1]:
            idx , _ = stack.pop()
            result[idx] = i
    return result




if __name__ == "__main__":

    tower_num = int(input())
    towers = list(map(int,sys.stdin.readline().split()))

    print(*searchTower(towers,tower_num))