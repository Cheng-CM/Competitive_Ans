T = int(input())
grid = [list(map(int,input().split())) for _ in range(T)]
flag = 1
for col in zip(*grid):
    if sum(col) != 0:
        print('NO')
        flag = 0
        break
if flag: print('YES')