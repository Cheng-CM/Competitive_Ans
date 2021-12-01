import math
def evenodd(c,d):
    return (c % 2 == 0 and d % 2 == 0) or (c % 2 != 0 and d % 2 != 0)
T = int(input())
for _ in range(T):
    c,d = list(map(int,input().split()))
    if abs(c-d) == 0:
        if c == d == 0:
            print('0')
        else:
            print('1')
    elif not evenodd(c,d):
        print('-1')
    else: print('2')
