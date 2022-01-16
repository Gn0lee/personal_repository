from collections import defaultdict

def solution(gems):
    answer = []
    tmp = 100000000
    target = len(set(gems))
    answer_dict = defaultdict(str)
    
    for i , gem in enumerate(gems):
        answer_dict[gem] = i+1
        
        if len(answer_dict) == target:
            a , b = min(answer_dict.values()), i+1
            if b-a < tmp:
                answer = [a,b]
                tmp = b-a
    
    # print(answer_dict.values())
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["A","A","A","B","B"]))
print(solution(["A"]))
print(solution(["A","B","B","B","B","B","B","C","B","A"]))