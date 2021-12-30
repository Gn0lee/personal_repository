def solution(n, computers):
    answer = 0
    parent = [k for k in range(n)]
    
    def find_parent(parent,x):
        if parent[x] == x:
            return parent[x]
        else:
            parent[x] = find_parent(parent,parent[x])
            return parent[x]
        
    def union_parent(parent,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    for j in range(n):
        for i in range(n):
            if i != j and computers[j][i] == 1:
                union_parent(parent,i,j)
    
    for l in range(n):
        find_parent(parent,l)
    
    answer = len(set(parent))
    return answer