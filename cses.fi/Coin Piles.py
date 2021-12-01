T = int(input())
for _ in range(T):
    a,b = list(map(int,input().split(' ')))
    if b > a: a,b = b,a
    if a > b * 2 or (a + b) % 3 != 0: print('NO')
    else: print('YES')