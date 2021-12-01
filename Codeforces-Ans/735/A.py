T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    if n == 2:
        print(a[0]*a[1])
    else:
        for i in range(1,n-1):
            ans = a[i] * max(a[i-1],a[i+1])
        print(ans)