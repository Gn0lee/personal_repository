import sys
input = sys.stdin.readline

def cal_max(n_zero,n_one,minus_list,plus_list):

    minus_list.sort()
    plus_list.sort(reverse = True)

    result = 0
    
    
    for _ in range(n_zero):
        if len(minus_list) % 2 == 0 :
            break
        minus_list.pop()

    a ,b  =  len(minus_list) , len(plus_list) 

    if a % 2 ==0:
        for i in range(0,a,2):
            result += minus_list[i] * minus_list[i+1]
    else:
        for j in range(0,a-1,2):
            result += minus_list[j] * minus_list[j+1]
        result += minus_list[a-1]

    if b % 2 == 0:
        for k in range(0,b,2):
            result += plus_list[k] * plus_list[k+1]
    else:
        for l in range(0,b-1,2):
            result += plus_list[l] * plus_list[l+1]
        result += plus_list[b-1]

    result += n_one

    return result



if __name__ == "__main__":
    n = int(input())

    minus_list = []
    plus_list = []
    n_zero = 0
    n_one = 0

    for _ in range(n):
        a = int(input())
        if a == 0 :
            n_zero += 1
            continue
        elif a == 1:
            n_one += 1
            continue
        elif a <0:
            minus_list.append(a)
            continue
        else:
            plus_list.append(a)

    print(cal_max(n_zero,n_one,minus_list,plus_list))