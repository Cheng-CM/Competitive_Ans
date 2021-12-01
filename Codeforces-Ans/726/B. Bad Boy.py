T = int(input())
for _ in range(T):
    n,m,i,j = list(map(int,input().split(" ")))
    c1,c2 = n/2,m/2
    if i >= c1 and j >= c2 or i < c1 and j < c2:
        print(1,m,n,1)
    else:
        print(1,1,n,m)