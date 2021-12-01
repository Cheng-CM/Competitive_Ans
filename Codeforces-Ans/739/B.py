T = int(input())
for _ in range(T):
    a,b,c = list(map(int,input().split()))
    num = abs(a-b)*2
    if a > num or b > num or c > num:
        print('-1')
    elif c + abs(a-b) <= num:
        print(c + abs(a-b))
    elif c - abs(a-b) > 0:
        print(c - abs(a-b))
    else:
        print('-1')