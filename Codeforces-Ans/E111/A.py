T = int(input())
for _ in range(T):
    n = int(input())
    i = 3
    k = 1
    ans = 1
    while k < n:
        k += i 
        ans += 1
        i += 2
    print(ans)