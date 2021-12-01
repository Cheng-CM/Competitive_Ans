n,m,a,b = list(map(int,input().split()))
if b == a and n % m > 0:
    print((n//m)*b+b)
elif b == a:
    print((n//m)*b)
elif m > n or m >= n and m == n:
    print(min(b,n*a))
elif m < n:
    if m*a < b:
        print(n*a)
    else:
        ans = (n//m)*b
        if n%m > 0:
            ans += min(b,(n%m)*a)
        print(ans)