T = int(input())
for _ in range(T):
    n = int(input())
    ans = [i for i in range(1,n+1)]
    if n % 2 == 0:
        for i in range(1,n,2):
            ans[i],ans[i-1] = ans[i-1],ans[i]
    else:
        for i in range(1,n-3,2):
            ans[i],ans[i-1] = ans[i-1],ans[i]
        ans[-3],ans[-1] = ans[-1],ans[-3]
        ans[-1],ans[-2] = ans[-2],ans[-1]
    print(*ans)