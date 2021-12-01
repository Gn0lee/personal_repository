import sys
input = sys.stdin.readline

inf = int(1e9)

def rev_bulb(arr , i):
    if i == n-1:
        arr[i-1] = 1 - arr[i-1]
        arr[i] = 1 - arr[i]
    
    else:
        arr[i] = 1 - arr[i]
        arr[i+1] = 1 - arr[i+1]
        arr[i-1] = 1 - arr[i-1] 

    return arr

def chk_bulb(arr,c):

    for a in range(n):
        if arr[a] != target[a]:
            return inf

    return c


if __name__ == "__main__":
    n = int(input())
    given1 = list(map(int,input().strip()))
    target = list(map(int,input().strip()))

    given2 = [ a for a in given1]

    given2[0] = 1 - given2[0]
    given2[1] = 1 - given2[1]
    
    count1 = 0
    for i in range(1,n):
        if given1[i-1] != target[i-1]:
            given1 = rev_bulb(given1,i)
            count1 += 1

    count2 = 1
    for j in range(1,n):
        if given2[j-1] != target[j-1]:
            given2 = rev_bulb(given2,j)
            count2 += 1

    # print(given1)
    # print(given2)

    count1 = chk_bulb(given1,count1)
    count2 = chk_bulb(given2,count2)

    if count2 == count1 == inf:
        print(-1)
    else:
        print(min(count1,count2))