def find_parent(parent,x): #노드의 루트를 찾는 함수
    
    #루트 노드를 찾을때 까지 재귀호출
    if parent[x] != x:
    #     return find_parent(parent,parent[x])
    # return x
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):

    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if b >a : #루트가 작은쪽으로 루트를 갱신해줌
        parent[b] = a
    else:
        parent[a] = b


v  = int(input())
parent = [0] * (v+1)
cost_list = [0] * (v+1)
for i in range(1,v+1):
    parent[i] = i

e = int(input())

infos = []

for i in range(e):
    a , b , cost= map(int, input().split())
    infos.append([cost,a,b])

infos.sort()

start , end = map(int, input().split())

for info in infos:
    if find_parent(parent,info[1]) != find_parent(parent,info[2]):
        union_parent(parent,info[1],info[2])
        cost_list[info[2]] = info[0]
    else:
        continue

# print(cost_list)
total = 0
for i in range(start,end+1):
    total += cost_list[i]
print(total)