from collections import deque
import sys



b = [1,2,3,4]

sys.stdout.write("<")
print(*b,sep=", ",end="")
sys.stdout.write(">")

