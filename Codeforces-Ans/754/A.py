T = int(input())
for _ in range(T): 
    a,b,c = list(map(int,input().split()))
    total = a+b+c
    print(abs(total-(round(total/3)*3)))
