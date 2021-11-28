import sys
input = sys.stdin.readline
from collections import deque

n , k = map(int,input().split())
elec_list = deque(list(map(int,input().split())))

multitab = set()

cnt = 0

while elec_list:
    now = elec_list.popleft()

    if len(multitab) < n:
        multitab.add(now)
        continue
    else:
        if now in multitab:
            continue
        else:
            left = -1
            chk = True
            for i in multitab:
                if i  not in elec_list:               
                    multitab.remove(i)
                    multitab.add(now)
                    cnt += 1
                    chk = False
                    break
                else:
                    if left < elec_list.index(i):
                        left = elec_list.index(i)
                        x = i
            if chk:
                multitab.remove(x)
                multitab.add(now)
                cnt += 1
            else:
                continue
print(cnt)
