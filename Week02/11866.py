from collections import deque
import sys

N,K = list(map(int,input().split()))

N_list = deque(range(1,N+1))
yose_list =[]
while N_list :
    
    N_list.rotate(-(K-1))
    yose_list.append(N_list.popleft())


sys.stdout.write("<")
print(*yose_list,sep=", ",end="")
sys.stdout.write(">")