from collections import Counter
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c,d = [],[]
    for i in range(n):
        if a[i] - b[i] > 0:
            c += [i+1] * (a[i] - b[i])
        elif a[i] - b[i] < 0:
            d += [i+1] * abs(a[i] - b[i])
    if len(c) == len(d):
        print(len(c))
        for i,j in zip(c,d):
            print(i,j) 
    else:
        print(-1)