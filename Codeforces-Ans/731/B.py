from collections import deque
T = int(input())
for _ in range(T):
    a = deque(input())
    n = len(a)
    while a:
        if ord(a[-1])-ord('a')+1 == n:
            a.pop()
            n -= 1
        elif ord(a[0])-ord('a')+1 == n:
            a.popleft()
            n -= 1
        else:
            break
    if len(a) > 0:
        print('NO')
    else:
        print('YES')