from functools import reduce
import sys
N = int(input())
soted_paper = [[0]*8 for _ in range(N)]
given_paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

global total_blue
total_blue = 0

global total_white
total_white = 0

def papercount(arr,jstart,jend,istart,iend):
    global total_blue
    global total_white
     
    blue = [0,0,0,0]
    white = [0,0,0,0]
    n = jend - jstart + 1
    if n == 2:
        if arr[jstart][istart] == arr[jstart][iend] and arr[jstart][iend] == arr[jend][istart] and arr[jend][istart] == arr[jend][iend]:
            if arr[jstart][istart] == 0:
                return [1,1,1,1] , [0,0,0,0] 
            elif arr[jstart][istart] == 1:
                return [0,0,0,0] , [1,1,1,1] 
        else:
            for j in range(jstart,jend+1):
                for i in range(istart,iend+1):
                    if arr[j][i] == 0:
                        total_white += 1
                    else:
                        total_blue += 1
            return  [1,0,1,0],[0,1,0,1]
    mj = (jstart +jend) // 2
    mi = (istart +iend) // 2

    
    chk = 0
    for j in range(jstart,mj+1):
        chk += reduce(lambda x , y: x+y,arr[j][istart:mi+1])
    if chk == (n**2)//4:
        blue[0] = blue[0] + 1
    elif chk == 0:
        white[0] = white[0] + 1
    chk = 0
    for j in range(jstart,mj+1):
        chk += reduce(lambda x , y: x+y,arr[j][mi+1:iend+1])
    if chk == (n**2)//4:
        blue[1] = blue[1] + 1
    elif chk == 0:
        white[1] = white[1] + 1    
    chk = 0
    for j in range(mj+1,jend+1):
        chk += reduce(lambda x , y: x+y,arr[j][istart:mi+1])
    if chk == (n**2)//4:
        blue[2] = blue[2] + 1
    elif chk == 0:
        white[2] = white[2] + 1
    chk = 0
    for x in range(mj+1,jend+1):
        chk += reduce(lambda x , y: x+y,arr[x][mi+1:iend+1])
    if chk == (n**2)//4:
        blue[3] = blue[3] + 1
    elif chk == 0:
        white[3] = white[3] + 1

    if white == [1,1,1,1]:
        return [1,1,1,1] , [0,0,0,0]
    elif blue == [1,1,1,1]:
        return  [0,0,0,0] , [1,1,1,1]

    total_blue += sum(blue)
    total_white += sum(white)
    return white, blue
    print(jstart,jend,istart,iend,end="  --->  ")
    print(white,blue,total_white,total_blue,end="    (흰, 파, 전체흰, 전체파)\n",sep=', ')
    # papercount(arr,n//2)

def mergeSort(arr,jstart,jend,istart,iend):
    global total_white
    global total_blue

    if jstart < jend or istart < iend:
        mj = (jstart +jend) // 2
        mi = (istart +iend) // 2
        result = papercount(arr,jstart,jend,istart,iend)
        if result[0] == [1,1,1,1]:
            total_white += 1
            return
        elif result[1] == [1,1,1,1]:
            total_blue += 1
            return
        else:        
            for i in range(4):
                if result[0][i] == 1 or result[1][i] == 1:
                    continue
                elif i == 0:
                    mergeSort(arr,jstart,mj,istart,mi)
                elif i == 1:
                    mergeSort(arr,jstart,mj,mi+1,iend)
                elif i == 2:
                    mergeSort(arr,mj+1,jend,istart,mi)
                else:
                    mergeSort(arr,mj+1,jend,mi+1,iend)
        

mergeSort(given_paper,0,N-1,0,N-1)
print(total_white)
print(total_blue)
# print(blue,white)