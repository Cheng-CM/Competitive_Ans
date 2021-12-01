T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    m = min(a)
    for i in range(n):
        a[i] = a[i]&m
    while m > min(a):
        m = min(a)
        for i in range(n):
            a[i] = a[i]&m
    print(m)
    