import sys

def caculateCircle(arr):
    coordinates = []
    stack = []
    for left , right in arr:
        coordinates.append([0,left])
        coordinates.append([1,right])

    coordinates = sorted(coordinates,reverse=True)
    coordinates = sorted(coordinates,key=lambda x: x[1])

    count = 1

    





    return count







if __name__ == "__main__":
    n = int(input())
    circles = []
    for _ in range(n):
        x ,  r = map(int,sys.stdin.readline().split())
        circles.append([x-r,x+r])

    print(caculateCircle(circles))