import sys
sys.setrecursionlimit(10**6)



def pre_post(start,end):
    if start > end:
        return
    
    root = pre_order[start]
    
    idx = start +1
    
    while idx <= end:
        if pre_order[idx] > root: #pre_order[start] 로 할 경우 start때 마다 검색을 해야해서 시간이 늘어난다. 한번 찾아놓은 값은 다시쓰도록하자
            break
        idx += 1

    pre_post(start+1,idx-1)
    
    pre_post(idx,end)
    
    sys.stdout.write(str(root)+"\n")



pre_order = []

while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

pre_post(0,len(pre_order)-1)

