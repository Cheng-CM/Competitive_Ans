T = int(input())
for _ in range(T):
    n,x,t = list(map(int,input().split(' ')))
    d = min(n-1,t//x)
    if d == 0: print(d)
    else: print(max(0,(n-d)*d) + (d*(d-1)//2))