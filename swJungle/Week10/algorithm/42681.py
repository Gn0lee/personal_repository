def solution(n, costs):
    answer = 0
    
    def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]
    
    def union_parent(parent,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
    
    costs.sort(key = lambda x : x[2],reverse = True)
    
    parent = [i for i in range(n)]
    
    while costs:
        j , k , cost = costs.pop()
        
        if find_parent(parent,j) != find_parent(parent,k):
            answer += cost
            union_parent(parent,j,k)
            
        if sum(parent) == 0:
            break
    
    return answer