pos = [0] * 3
flag = [False] * 3

def put():
    for i in range(3):
        print(f'{pos[i]:2}', end='')
    print()
def set(i):
    for j in range(3):
        if not flag[j]:
            pos[i] = j
            if i == 2:
                put()
            else:
                flag[j] = True
                set(i+1)
                flag[j] = False
set(0)
        