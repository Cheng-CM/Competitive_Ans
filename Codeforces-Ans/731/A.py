T = int(input())
for _ in range(T):
    em = input()
    print(em)
    x1,y1 = list(map(int,input().split()))
    x2,y2 = list(map(int,input().split()))
    x3,y3 = list(map(int,input().split()))
    if x1 == x2 == x3 and (y1 > y3 > y2 or y2 > y3 > y1):
        print(abs(y1-y2)+2)
    elif y1 == y2 == y3 and (x1 > x3 > x2 or x2 > x3 > x1):
        print(abs(x1-x2)+2)
    else:
        print(abs(x1-x2)+abs(y1-y2))