from itertools import combinations

def solution(n, weak, dist):
    answer = 0
    num_people = len(dist)
    num_chk = len(weak)
    dist.sort()
    max_dist = dist[-1]
    set_weak = set(weak)
    routes = []
    
    for x in weak:
        routes.append([0,set([x])])

    for start, end in combinations(range(num_chk),2):
        if weak[end] - weak[start] <= max_dist:
            tmp =set()
            for i in range(start,end+1):
                tmp.add(weak[i])
            routes.append([weak[end] - weak[start],tmp])
        if n - (weak[end] - weak[start]) <= max_dist:
            tmp = set()
            for j in range(start,end-num_chk-1,-1):
                tmp.add(weak[j])
            routes.append([n - weak[end] + weak[start],tmp])
    
    routes.sort(key= lambda x:x[0],reverse=True)
    
    for k in range(1,num_people+1):
        for route in combinations(routes,k):
            point = num_people -1
            chk = set()
            for length, done in route:
                if length <= dist[point]:
                    point -= 1
                    chk = chk | done
                else:
                    break
            if chk == set_weak:
                return k


    return -1

# a = set([1,2,3])
# b = [2,3,1]

# print(a == set(b))
# print(b)

print(solution(12,[1,5,6,10],[1,2,3,4]))
print(solution(12,[1,3,4,9,10],[3,5,7]))
print(solution(200,[0,100],[1,1]))