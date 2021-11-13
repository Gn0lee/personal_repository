import sys
testcase = int(sys.stdin.readline())
testlist = list(map(int,sys.stdin.readline().split()))
testlist.sort()
pos = [0]*testcase
flag = [False] * testcase
max_num = testcase * (max(testlist)-min(testlist))
abslist = [0] * testcase * (max(testlist)-min(testlist))
# abslist = []

def totalABS(a,b):
    combination_list = [b[i] for i in a]
    diffList = list(map(lambda x : abs(combination_list[x]-combination_list[x+1]),range(len(combination_list)-1)))
    # print(combination_list, end='\t\t')
    # print(diffList)
    return sum(diffList)

def printPos (c):
    for i in range(c):
        print(f'{pos[i] :2}', end='')
    print()

def set(i,n):
    for j in range(n):
        if not flag[j]:
            pos[i] = j
            if i == n-1:
                abslist[totalABS(pos,testlist)] = 1
                # print()
                # abslist.append(totalABS(pos,testlist))
                
    
            else:
                flag[j] = True
                set(i+1,n)
                flag[j] = False

set(0,testcase)

for i in range(max_num-1,0,-1):
    if abslist[i] == 1:
        print(i)
        break