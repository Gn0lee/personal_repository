import sys
from collections import deque

text = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

ans = []

for i in text:
    ans.append(i)

    if len(bomb) <= len(ans):
        chk = True
        for j in range(-1,-len(bomb)-1,-1):
            if bomb[j] != ans[j]:
                chk = False
                break
        if chk:
            for _ in range(len(bomb)):
                ans.pop()



              
if not ans:
    print("FRULA")
else:
    print(*ans,sep="")   




