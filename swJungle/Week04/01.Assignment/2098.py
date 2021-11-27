import sys
input = sys.stdin.readline
inf = int(1e9)
sys.setrecursionlimit(10**9)


def tsp(cost,start = 0):
    VISITED_ALL = (1 << N) - 1
    cache = [[None]*(1 << N) for _ in range(N)]

    def cal_min_cost(current,visited):
        
        if visited == VISITED_ALL:
            return cost[current][start] or inf

        if cache[current][visited] != None:
            return  cache[current][visited]

        tmp = inf

        for next in range(N):
            if visited & (1<<next) == 0 and cost[current][next] != 0:
                tmp = min(tmp,cal_min_cost(next,visited|(1<<next))+cost[current][next])

        cache[current][visited] = tmp

        return tmp

    return cal_min_cost(start,1<<start)


N = int(input())

cost_list = []

for _ in range(N):
    cost_list.append(list(map(int,input().split())))


print(tsp(cost_list))