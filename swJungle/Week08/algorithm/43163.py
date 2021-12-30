
from collections import defaultdict, deque

def solution(begin, target, words):
    
    def nextstrs(a,words):
        
        tmp = []
        n = len(a)
        for word in words:
            count = 0
            for i in range(n):
                if a[i] == word[i]:
                    count += 1
            if count == n-1:
                tmp.append(word)
        
        return tmp
    
    def bfs(begin,target,words):
        q = deque(nextstrs(begin,words))
        chk = defaultdict(lambda: False)
        
        count = 0
        min_val = int(1e9)

        while q:
            count += 1
            for _ in range(len(q)):
                now = q.popleft()
                chk[now] = True
            if now == target:
                min_val = min(min_val,count)
            for next in nextstrs(now,words):
                if not chk[next]:
                    q.append(next)
        
        if min_val == int(1e9):
            return 0
        else:
            return min_val

    answer = bfs(begin,target,words)
        
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "hhh", ["hhh","hht"]))

# begin = "hit"
# target = "hhh"
# wodrs = ["hhh","hht"]
# return = 2