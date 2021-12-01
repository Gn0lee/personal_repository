import sys
input = sys.stdin.readline

def rev_matrix(j,i,a):

    for y in range(j,j+3):
        for x in range(i,i+3):
            a[y][x] = 1 - a[y][x]

    return a


def chk_matrix(a,b,n,m):
    for y in range(n):
        for x in range(m):
            if a[y][x] != b[y][x]:
                return False

    return True


if __name__ == "__main__":
    n , m = map(int,input().split())

    A = [list(map(int,input().strip())) for _ in range(n)]
    B = [list(map(int,input().strip())) for _ in range(n)]
    count = 0
    
    for y in range(n-2):
        for x in range(m-2):
            if A[y][x] != B[y][x]:
                A = rev_matrix(y,x,A)
                count += 1

    if chk_matrix(A,B,n,m):
        print(count)
    else:
        print(-1)