def solution(numbers):
    answer = 0
    from itertools import permutations
    from math import sqrt
    
    # 소수 확인하는 함수
    def chk_prime_num(x):
        if x == 0 or x == 1:
            return False
        for i in range(2,int(sqrt(x))+1):
            if x % i ==0:
                return False
        return True
    
    permu_nums = set()
    
    # 순열로 조합하여 가능한 경우를 permu_nums에 add
    for i in range(1,8):        
        for j in permutations(numbers,i):
            if j[0] == '0':
                continue
            permu_str =''
            for k in j:
                permu_str += str(k)
                permu_nums.add(int(permu_str))
    
    for permu_num in permu_nums:
        if chk_prime_num(permu_num):
            answer+=1
    
    return answer

print(solution('011'))