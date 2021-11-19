def find_parent(parent,x): #노드의 루트를 찾는 함수
    
    #루트 노드를 찾을때 까지 재귀호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

    ## parnent[x] = find_parent(parent,parent[x])
    ## return parent[x]
def union_parent(parent,a,b):

    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if b >a : #루트가 작은쪽으로 루트를 갱신해줌
        parent[b] = a
    else:
        parent[a] = b


v , e = int(input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a , b = map(int, input().split())

    