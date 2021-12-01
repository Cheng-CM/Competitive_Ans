from collections import Counter
T = int(input())
for _ in range(T):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    c = Counter(s)
    total = n // k * n
    ans = []
    for i in a:
        c[i] += 1
        if c[i] <= k:
            if ck[c[i]] < th:
                ans.append(c[i])
            else
        else:
            ans.append(0)
    print(*ans)