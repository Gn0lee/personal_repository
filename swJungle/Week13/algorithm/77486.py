from collections import defaultdict

def solution(enrolls, referrals, sellers, amounts):
    enroll_referral_dict = defaultdict(str)
    profit_dict = defaultdict(lambda : 0)
    n = len(enrolls)
    answer = [0] * n
    
    for enroll,referral in zip(enrolls,referrals):
        enroll_referral_dict[enroll] = referral
    
    for seller,amount in zip(sellers,amounts):
        tmp = amount * 100
        
        while tmp >= 1 and seller != "-":
            profit_dict[seller] += tmp - (tmp // 10)
            seller = enroll_referral_dict[seller]
            tmp = tmp//10
    
    for index,final_enroll in enumerate(enrolls):
        answer[index] = profit_dict[final_enroll]

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))