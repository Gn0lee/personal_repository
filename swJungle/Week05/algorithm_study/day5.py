def solution(numbers):
    answer = 0
    from itertools import permutations
    from math import sqrt
    
    def chk_prime_num(x):
        if x == 0 or x == 1:
            return False
        for i in range(2,int(sqrt(x))+1):
            if x % i ==0:
                return False
        return True
    
    l = set()
    
    for i in range(1,8):        
        for j in permutations(numbers,i):
            if j[0] == '0':
                continue
            permu_num =''
            for k in j:
                permu_num += str(k)
                l.add(int(permu_num))
    
    for x in l:
        if chk_prime_num(x):
            answer+=1
    
    return answer

print(solution('011'))