import sys


def multi(arr1,arr2,size):
    arr3 = [ [0]* size  for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for l in range(size):
                arr3[i][j] += arr1[i][l] * arr2[l][j] % 1000 
    return arr3

def square(arr,n):
    size = len(arr)
    if n  == 1:
        return arr
    elif n % 2 == 0:
        squ_arr = square(arr,n//2)
        return multi(squ_arr,squ_arr,size)
    else:
        squ_arr = square(arr,n//2)
        return multi(arr,multi(squ_arr,squ_arr,size),size)


if __name__ == "__main__":

    n , b = list(map(int, sys.stdin.readline().split()))
    A = [ [0]* n  for _ in range(n)]
    C = [ [0]* n  for _ in range(n)]
    for i in range(n):
        A[i] = list(map(int, sys.stdin.readline().split()))

    C = square(A,b)
    for i in range(n):
        for j in range(n):
            print(C[i][j]%1000,end= " ")
        print()
