import collections
import heapq
T = int(input())
for _ in range(T):
    n = int(input())
    d = collections.defaultdict(collections.Counter)
    grid = [[(r,i+1) for r in list(map(int,input().split()))] for i in range(n)]
    if n == 1:
        print(1)
    else:
        for col in zip(*grid):
            a = list(col)
            heapq.heapify(a)
            while a:
                curr = heapq.heappop(a)
                for i in a:
                    d[curr[1]][i[1]] += 1
        flag = 0
        for i in d:
            if all(d[i][j] >= 3 for j in d[i]):
                flag = 1
                print(i)
                break
        if not flag: print(-1)
        print(d)