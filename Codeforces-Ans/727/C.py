import heapq
n,k,x = list(map(int,input().split()))
a = list(map(int,input().split()))
if n == 1:
    print('1')
else:
    heapq.heapify(a)
    cur = heapq.heappop(a)
    q = []
    while a:
        nex = heapq.heappop(a)
        if nex - cur > x:
            q.append(nex - cur)
        cur = nex
    ans = len(q)+1
    if k:
        for i in q:
            cur = i // x
            if k >= cur:
                ans -= 1
                k -= cur
            else:
                break
    print(ans)