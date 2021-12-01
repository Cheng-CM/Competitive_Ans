from collections import deque
T = int(input())
for _ in range(T):
    em = input()
    k,m,p = list(map(int,input().split()))
    a = deque(map(int,input().split()))
    b = deque(map(int,input().split()))
    ans = []
    while a or b:
        if a:
            if a[0] == 0:
                ans.append(a.popleft())
                k += 1
            elif a[0] <= k:
                ans.append(a.popleft())
        elif b:
            if b[0] == 0:
                ans.append(b.popleft())
                k += 1
            elif b[0] <= k:
                ans.append(b.popleft())
        if ((a and a[0] > k) or not a) and ((b and b[0] > k) or not b):
            break
    if a or b:
        print(-1)
    else:
        print(*ans)