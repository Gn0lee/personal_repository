def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        given_arr = [ array[x-1] for x in range(i,j+1)]
        given_arr.sort()
        answer.append(given_arr[k-1])
    
    return answer