import math
T = int(input())
for _ in range(T):
    n,m = map(int,input().split(' '))
    p = min(n,m)
    if p != 1:
        print('2')
    else:
        print('1')