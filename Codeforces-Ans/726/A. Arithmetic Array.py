T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split(" ")))
    c = sum(a)
    if c < n:
        print('1')
    elif c == n:
        print('0')
    else:
        print(c-n)
    