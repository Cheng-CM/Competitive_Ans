from functools import reduce
def XOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0

T = int(input())
for _ in range(T):
    a,b = list(map(int,input().split()))
    res = XOR(a-1) ^ b
    res = res ^ 0
    i = a+1
    while res != b:
        res = res ^ i
        a += 1
        i += 1
    print(a)
