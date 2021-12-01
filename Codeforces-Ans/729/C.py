T = int(input())
mod = 10 ** 9 + 7
for _ in range(T):
    n = int(input())
    if n == 1: print('2')
    elif n == 2: print('5')
    else: print('Ans', (4+(n*(n+1)//2)-n) % mod)