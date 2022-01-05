from collections import defaultdict

def solution(N, number):

    n_list = defaultdict(set)
    
    for i in range(1,9):
        x = (10**i-1)//9
        n_list[i].add(N*x)
        
    for answer in range(1,9):        
        if number in n_list[answer]:
            return answer
        for a in n_list[answer]:
            n_list[answer+1].add(a+N)
            n_list[answer+1].add(a*N)
            x , y ,z = a//N, N//a, N-a
            if x != 0:    
                n_list[answer+1].add(x)
            else:
                n_list[answer+1].add(y)
            if z > 0:
                n_list[answer+1].add(z)
            elif z < 0:
                n_list[answer+1].add(-z)

        for b in range(1,(answer+1)//2+1):
            c = (answer+1) - b
            
            if b == c:
                continue

            for x in n_list[b]:
                for y in n_list[c]:
                    n_list[answer+1].add(x+y)
                    n_list[answer+1].add(x*y)
                    if x // y != 0:
                        n_list[answer+1].add(x//y)
                    else:
                        n_list[answer+1].add(y//x)
                    if x-y > 0:
                        n_list[answer+1].add(x-y)
                    elif x-y < 0:
                        n_list[answer+1].add(y-x)           
    answer = -1
    return answer

