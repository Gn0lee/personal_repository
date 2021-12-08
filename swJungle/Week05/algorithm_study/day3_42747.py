citations = [23, 1, 25, 21, 34, 21]


answer = 0
citation_list = [0]*10001

for i in citations:
    citation_list[i] += 1

for j in citations:
    if sum(citation_list[j:]) >= j and sum(citation_list[:j+1])<=j: 
        answer = max(answer,j)

print(answer)
