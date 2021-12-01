n = int(input())
ans = 0
while n > 0:
    ans += 1
    if (n - 100) >= 0:
        n -= 100
    elif (n - 20) >= 0:
        n -= 20
    elif (n - 10) >= 0:
        n -= 10
    elif (n - 5) >= 0:
        n -= 5
    elif (n - 1) >= 0:
        n -= 1
print(ans,flush=True)