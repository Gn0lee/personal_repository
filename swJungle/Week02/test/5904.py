import sys


n = int(input())

def find_len_moo(x):
    k = 0
    l = 3
    while l < x:
        k = k +1
        l = 2*l+3+k
    return k

def cal_len_moo(x):
    k = 0
    l = 3
    while k < x:
        k = k +1
        l = 2*l+3+k
    return l




def find_k(n,k):
    before_s = cal_len_moo(k-1)
    if k == 0:
        if n == 1:
            return "m"
        else:
            return "o"

    if n <= before_s:
        return find_k(n,k-1)
        
    elif n == before_s+1:
        return "m"
    elif before_s+1<n <= k+3+before_s:
        return "o"
    else:
        return find_k(n-before_s-k-3,k-1)


# print(find_len_moo(11))

print(find_k(n,find_len_moo(n)))