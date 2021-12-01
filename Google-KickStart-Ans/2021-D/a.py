from collections import Counter
T = int(input())
for t in range(T):
    r1 = list(map(int,input().split(" ")))
    r2 = list(map(int,input().split(" ")))
    r3 = list(map(int,input().split(" ")))
    c = Counter()
    def isA(i,j,k):
        return abs(i-j) == abs(j-k) and (i != k or i == j == k)
    ans = 0
    if isA(*r1): ans += 1
    if isA(*r3): ans += 1
    if isA(r1[0],r2[0],r3[0]): ans += 1
    if isA(r1[-1],r2[-1],r3[-1]): ans += 1
    if abs(r1[0] - r3[-1]) % 2 == 0:
        c[(abs(r1[0] - r3[-1])//2)+min(r1[0],r3[-1])] += 1
    if abs(r1[1] - r3[1]) % 2 == 0:
        c[(abs(r1[1] - r3[1])//2)+min(r1[1],r3[1])] += 1
    if abs(r2[0] - r2[-1]) % 2 == 0:
        c[(abs(r2[0] - r2[-1])//2)+min(r2[0],r2[-1])] += 1
    if abs(r3[0] - r1[-1]) % 2 == 0:
        c[(abs(r3[0] - r1[-1])//2)+min(r3[0],r1[-1])] += 1
    ans += max(c.items(),key = lambda x:x[1])[1]
    print("Case #"+ str(t+1) +":",str(ans),flush=True)