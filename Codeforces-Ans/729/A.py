T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    o,e = 0,0
    for i in a:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    if o == e:
        print('Yes')
    else:
        print('No')