import math
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0 for _ in range(2*n+1)]
    a = list(map(int,input().split()))
    for i,v in enumerate(a):
        arr[v] = i+1
    ans = 0
    for i in range(3,n*2):
        s = int(math.sqrt(i))
        for j in range(1, s + 1):
            if i % j == 0 and i != j * j and arr[j] + arr[i//j] == i:
                ans += 1
    print(ans)