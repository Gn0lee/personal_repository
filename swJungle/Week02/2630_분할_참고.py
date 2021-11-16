import sys
global blue
blue = 0
global white
white = 0

def quadTree(y,x,n):
    global blue
    global white
    start = n_list[y][x]
    chk = False
    
    for j in range(y,y+n):
        if chk: ##이미 한개라도 다르면 break
            break
        
        for i in range(x,x+n):
            if start != n_list[j][i]:
                quadTree(y,x,n//2)
                quadTree(y,x+n//2,n//2)
                quadTree(y+n//2,x,n//2)
                quadTree(y+n//2,x+n//2,n//2)
                chk = True

                break
    if not chk:
        if start == 1:
            blue += 1
        else:
            white += 1

    return


if __name__ == "__main__":
    
    N = int(input())
    n_list = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    quadTree(0,0,N)

    print(white)
    print(blue)


