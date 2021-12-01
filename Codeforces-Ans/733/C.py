import math
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    k = n - math.floor(n/4)
    print(k)