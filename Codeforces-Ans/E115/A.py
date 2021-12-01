T = int(input())
for _ in range(T):
    n = int(input())
    a,b = input(),input()
    flag=1
    for i,j in zip(a,b):
        if i == j == '1':
            print('NO')
            flag=0
            break
    if flag==1:
        print('YES')