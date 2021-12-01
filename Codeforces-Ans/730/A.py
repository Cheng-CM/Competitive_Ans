def gcd(a,b):
    while b:
        a %= b
        a,b = b,a
    return a

T = int(input())
for _ in range(T):
    a,b = list(map(int,input().split()))
    if a == b:
        print('0 0')
    else:
        f = abs(a-b)
        if b%f != 0:
            print(f,f-(b%f))
        else:
            print(f,0)