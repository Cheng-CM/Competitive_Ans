from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
ans = 0
for i in range(n):
    curr = c[1]
    for j in range(i,n):
        if a[j] == 0:
            curr += 1
        else:
            curr -= 1
        ans = max(ans,curr)
print(ans)