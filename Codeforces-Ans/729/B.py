T = int(input())
for _ in range(T):
    n,a,b = list(map(int,input().split()))
    while n > 0:
        if n%a == 0 or n%b == 1:
            print('Yes',divmod(n,a),divmod(n,b))
            break
        n -= b
    else:
        print('No')
        