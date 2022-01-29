from functools import reduce

def solution(key, lock):
    n_lock = len(lock)
    n_key = len(key)

    def rotate(y):
        z = [ list(x) for x in zip(*reversed(y))]    
        return z

    def chk_open(mv_y,mv_x,r_key):
        board = [[0]*(2*n_key+n_lock -2) for _ in range((2*n_key+n_lock -2))]

        for j in range(n_lock):
            for i in range(n_lock):
                board[j+n_key-1][i+n_key-1] = lock[j][i]


        for k in range(n_key):
            for l in range(n_key):               
                board[k+mv_y][l+mv_x] += r_key[k][l]
        
        # print(*board,sep="\n")
        # print()
        
        for n in range(n_lock):
            if reduce(lambda x, y : x * y ,board[n+n_key-1][n_key-1:n_lock+n_key-1]) != 1:
                return False

        return True   
    
    for _ in range(4):
        
        for y in range(n_key+n_lock-1):
            for x in range(n_key+n_lock-1):
                if chk_open(y,x,key):
                    return True
        key = rotate(key)

    return False