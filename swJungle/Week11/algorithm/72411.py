from itertools import combinations
from collections import defaultdict
# def solution(orders, course):
#     answer = []
#     menus1 = defaultdict(lambda : 0)
#     length = [0] * 11
#     for order in orders:
#         length[len(order)] += 1
#         for menu in order:
#             menus1[menu] += 1
#     menus = []
#     for key in menus1.keys():
#         if menus1[key] >= 2:
#             menus.append(key)

#     for n in course:
#         tmp = defaultdict(list)
#         if sum(length[n:]) <2:
#             continue
#         for combi in combinations(menus,n):
#             combi1 = set(combi)
#             count,index = 0,0
#             for sonnim in orders:
#                 if combi1 <= set(sonnim):
#                     count += 1
#             if count >= 2:          
#                 tmp[count].append(sorted(combi))
#         if tmp:
#             x = max(tmp.keys())
#             for y in tmp[x]:
#                 answer.append("".join(y))
        
#     answer.sort()
#     return answer


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

def solution(orders, course):
    answer = []
    
    for n in course:
        sub = defaultdict(lambda : 0)
        for order in orders:
            order1 = "".join(sorted(order))
            if len(order) >=n:
                for i in combinations(order1,n):
                    sub[i] += 1

        if sub:
            max_val = max(sub.values())
            if max_val >= 2:
                for key,value in sub.items():
                    if value == max_val:
                        answer.append("".join(key))

    answer.sort()



    return answer

# a = set()
# a.add(1)
# a.add(1)
# a.add(3)
# a.add(4)

# b = (1,2,3,1)
# a = list(a)
# b = set(b)
# print(b)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

