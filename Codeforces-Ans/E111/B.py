from itertools import groupby
T = int(input())
for _ in range(T):
    n,a,b = list(map(int,input().split()))
    s = input()
    arr = []
    zero,one = 0,0
    for k, g in groupby(s):
        l = list(g)
        arr.append((l[0],len(l)))
        if l[0] == '0':
            zero += len(l)
        else:
            one += len(l)
    if zero > one:
        if a > b:
            for i,v in arr:
                