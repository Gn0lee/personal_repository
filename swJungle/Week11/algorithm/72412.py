from collections import defaultdict,deque
from itertools import combinations
def solution(info, query):
    answer = []
    
    def make_table(info):
        people = defaultdict(list)
        
        for p in info:
            p_list = p.split()
            grade = int(p_list.pop())
            for n in range(5):
                for i in list(combinations(p_list,n)):
                    people["".join(i)].append(grade)
        return people
    
    def make_q_list(r):
        
        r_list = [ i for i in r.split() if i != "and" and i != "-"]
    
        if len(r_list) == 0:
            return ["",grade]
        r_grade = int(r_list.pop())
        
        return ["".join(r_list),r_grade]

    def cal_ans(key,people,grade):
        tmp = 0
    
        
        n = len(people[key])
        start , end = 0, n
        while start != end and start != n:
            mid = (start + end) // 2
            if people[key][mid] >= grade:
                end = mid
            else:
                start = mid + 1
        tmp += n - start
        return tmp
  
    people = make_table(info)

    for value in people.values():
        value.sort()

    for request in query:
        key , grade = make_q_list(request)
        
        answer.append(cal_ans(key,people,grade))    
                
    return answer



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


#from collections import defaultdict,deque
# def solution(info, query):
#     answer = []
#     dict_info = {
#         "cpp" : -1,
#         "java" : -2,
#         "python" : -3,
#         "backend" : 1,
#         "frontend" : 0,
#         "junior" : 1,
#         "senior" : 0,
#         "chicken" : 1,
#         "pizza" : 0,
#         "-" : 0
#     }
    
#     def make_table(info,dict_info):
#         people = [[] for _ in range(42)]
        
#         for p in info:
#             x = 1
#             lang , area , year , food , grade = p.split()
#             x = (x << 2) + dict_info[lang]
#             x = (x << 1) + dict_info[area]
#             x = (x << 1) + dict_info[year]
#             x = (x << 1) + dict_info[food]
#             people[x].append(int(grade))
#         return people
    
#     def make_q_list(r,dict_info):
#         r = r.replace(" and","")
#         r_lang , r_area , r_year, r_food, r_grade = r.split()
#         r_grade = int(r_grade)
#         x_list = deque([])
    
#         if r_lang == "-":
#             x_list = deque([1,2,3])
#         else:
#             x_list.append((1 << 2) + dict_info[r_lang])
#         if r_area == "-":            
#             for _ in range(len(x_list)):
#                 now = x_list.pop()
#                 x_list.appendleft((now<<1)+1)
#                 x_list.appendleft((now<<1))
#         else:
#             for i in range(len(x_list)):
#                 x_list[i] = (x_list[i]<<1) + dict_info[r_area]
#         if r_year == "-":            
#             for _ in range(len(x_list)):
#                 now = x_list.pop()
#                 x_list.appendleft((now<<1)+1)
#                 x_list.appendleft((now<<1))
#         else:
#             for i in range(len(x_list)):
#                 x_list[i] = (x_list[i]<<1) + dict_info[r_year]
#         if r_food == "-":            
#             for _ in range(len(x_list)):
#                 now = x_list.pop()
#                 x_list.appendleft((now<<1)+1)
#                 x_list.appendleft((now<<1))
#         else:
#             for i in range(len(x_list)):
#                 x_list[i] = (x_list[i]<<1) + dict_info[r_food]

#         return [x_list,r_grade]

#     def cal_ans(r_list,people,grade):
#         tmp = 0
#         for y in r_list:
#             people[y].sort()
#             n = len(people[y])
#             start , end = 0, n
#             while start != end and start != n:
#                 mid = (start + end) // 2
#                 if people[y][mid] >= grade:
#                     end = mid
#                 else:
#                     start = mid + 1
#             tmp += n - start
#         return tmp
  
#     people = make_table(info,dict_info)

#     for request in query:
#         r_list , grade = make_q_list(request,dict_info)
        
#         answer.append(cal_ans(r_list,people,grade))    
                
#     return answer

