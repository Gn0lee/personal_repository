import sys


def calDistance(point0, point1):

    return (point0[0]-point1[0]) ** 2 + (point0[1]-point1[1]) ** 2

def searchPoint(arr):
    if len(arr) == 2:
        return calDistance(arr[0],arr[1])
    if len(arr) == 3:
        return min(calDistance(arr[0],arr[1]),calDistance(arr[1],arr[2]),calDistance(arr[0],arr[2]))
    
    mid = len(arr) // 2

    d = min(searchPoint(arr[:mid]),searchPoint(arr[mid:]))

    check = []

    for i in arr:
        if (i[0]-arr[mid][0]) ** 2 < d:
            check.append(i)
    check.sort(key=lambda x: x[1])

    for i in range(len(check)-1):
        for j in range(i+1,len(check)):
            if (check[i][1] - check[j][1]) ** 2 < d:
                d = min(d,calDistance(check[i],check[j]))
            else:
                break
    return d



if __name__ == "__main__":
    n = int(input())
    point = []
    for i in range(n):
        x , y = list(map(int,sys.stdin.readline().split()))
        point.append((x,y))

    point.sort(key=lambda x : x[0])
    d = searchPoint(point)
    print(d) 