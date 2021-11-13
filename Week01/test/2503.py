from itertools import combinations, permutations

times = int(input())
minhyuk_list = [list(map(int ,input().split())) for _ in range(times)]

ans = 0
for case in permutations([1,2,3,4,5,6,7,8,9],3):
    cnt = 0
    # print(case,end="        ")
    for minhyuk in minhyuk_list:
        strike_cal = 0
        ball_cal = 0
        minhyuk_1 = minhyuk[0] % 10
        minhyuk_100 = minhyuk[0] // 100
        minhyuk_10 = (minhyuk[0] - minhyuk_100*100 -minhyuk_1)//10
        strike_given = minhyuk[1]
        ball_given = minhyuk[2]
        
        if minhyuk_100 == case[0]:
            strike_cal += 1
        elif case[0] == minhyuk_1 or case[0] == minhyuk_10:
            ball_cal += 1
        if minhyuk_10 == case[1]:
            strike_cal += 1
        elif case[1] == minhyuk_1 or case[1] == minhyuk_100:
            ball_cal += 1
        if minhyuk_1 == case[2]:
            strike_cal += 1
        elif case[2] == minhyuk_100 or case[2] == minhyuk_10:
            ball_cal += 1
        if strike_cal != strike_given or ball_cal != ball_given:
            continue
        cnt += 1
    # print(cnt)
    if cnt == times:
        ans += 1

print(ans)