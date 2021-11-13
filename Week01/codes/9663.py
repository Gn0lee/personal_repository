import sys
testcase = int(sys.stdin.readline())
global cnt
cnt = 0

pos = [0]*testcase
flag = [False] * testcase
flag_a = [False] * ((testcase * 2)-1)
flag_b = [False] * ((testcase * 2)-1)
count_list = []
def printPos (c):
    # count_list[c] = 1
    for i in range(c):
        print(f'{pos[i] :2}', end='')
    print()
#     count_list.append(pos)
def totalABS():
    
    # print(combination_list, end='\t\t')
    # print(diffList)
    return 1

def set(i,n,c):
    global cnt
    for j in range(n):
        if flag[j] == False and flag_a[j+i] == False and flag_b[n-1-j+i] == False:
            pos[i] = j
            if i == n-1:
                # count_list[c] = 1 
                # printPos(n)
                # c += 1
                cnt += 1
                # count_list.append(pos)
            else:
                flag[j] = True
                flag_a[j+i] = True
                flag_b[n-1-j+i] = True
                set(i+1,n,c)
                flag[j] = False
                flag_a[j+i] = False
                flag_b[n-1-j+i] = False

set(0,testcase,0)
# print(len(count_list))
print(cnt)
