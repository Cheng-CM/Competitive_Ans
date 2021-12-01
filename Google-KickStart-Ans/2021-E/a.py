from collections import deque
T = int(input())
for t in range(T):
    s = input()
    dq = deque(s)
    ans = ''
    i = 0
    dq_check = 0
    while dq:
        if dq[-1] != s[i]:
            ans += dq.pop()
            i += 1
            dq_check = 0
        else:
            dq_check += 1
            if dq_check == len(dq):
                ans = "IMPOSSIBLE"
                break
            dq.appendleft(dq.pop())
    print("Case #"+ str(t+1) +":",str(ans),flush=True)