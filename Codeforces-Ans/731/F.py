def gcd(a,b):
    while b:
        a %= b
        a,b = b,a
    return a

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    while any(i != a[0] for i in a):
        b = [gcd(a[i],a[i+1]) for i in range(n-1)]
        b.append(gcd(a[0],a[-1]))
        a = b
        ans += 1
    print(ans)