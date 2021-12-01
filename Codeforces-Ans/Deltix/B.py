from collections import Counter
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    even,odd = 0,0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
        a[i] = a[i] % 2
    if abs(even-odd) > 1:
        print('-1')
    else:
        ans = 0
        for i in range(n):
            if (i + 1 < n and a[i] == a[i + 1]) or i >= 1 and a[i] == a[i - 1]:
                ans += 1
            if (i + 1 < n and a[i] != a[i + 1]) or i >= 1 and a[i] != a[i - 1]:
                ans -= 1
        print(ans)