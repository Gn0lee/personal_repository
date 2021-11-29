import sys

cache = [[[None]*21 for _ in range(21)] for __ in range(21)]
    
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a == 0 or b ==0 or c ==0:
                cache[a][b][c] = 1
            elif c > b > a:
                if c != 1 and b !=1:
                    cache[a][b][c] = cache[a][b][c-1] + cache[a][b-1][c-1] - cache[a][b-1][c]
                elif c == 1 and b !=1:
                    cache[a][b][c] = 1 + 1 - cache[a][b-1][c]
                elif c != 1 and b ==1:
                    cache[a][b][c] = cache[a][b][c-1]
                elif c == 1 and b ==1:
                    cache[a][b][c] = 1
            else:
                if a == 1:
                    cache[a][b][c] = 2
                else:
                    if c == 1 and b ==1:
                        cache[a][b][c] = cache[a-1][b][c] + 1
                    elif c == 1:
                        cache[a][b][c] = cache[a-1][b][c] + cache[a-1][b-1][c]
                    elif b == 1 :
                        cache[a][b][c] = cache[a-1][b][c] +cache[a-1][b][c-1]
                    else:
                        cache[a][b][c] = cache[a-1][b][c] + cache[a-1][b-1][c] +cache[a-1][b][c-1] - cache[a-1][b-1][c-1]

def w(x , y , z):

    if x <= 0 or y <= 0 or z <= 0:
        return 1
    
    elif x > 20 or y > 20 or z > 20:
        return cache[20][20][20]

    else:
        return cache[x][y][z]

while True:

    a , b , c = map(int,input().split())

    if a == -1 and b == -1 and c == -1 :
        exit(0)

    ans = w(a , b , c)

    print('w({}, {}, {}) = {}'.format(a,b,c,ans))