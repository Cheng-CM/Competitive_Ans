T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    su = sum(a)
    k = su/n
    b = [(su-a[i])/(n-1) for i in range(n)]
    print(su,k,a,b)