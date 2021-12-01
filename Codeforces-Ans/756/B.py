T = int(input())
for t in range(T):
    a,b = map(int,input().split(' '))
    if min(a,b) == 0:
        print('0')
    else:
        print(min((a+b)//4,min(a,b)))