T = int(input())
for _ in range(T):
    n = int(input())
    d,m = divmod(n,3)
    if m == 1:
        print(d+1,d)
    elif m == 2:
        print(d,d+1)
    else:
        print(d,d)