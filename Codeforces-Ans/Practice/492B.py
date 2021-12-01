n,l = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
ans = max(a[0]-0,l-a[-1])
for i in range(len(a)-1):
    ans = max(ans,(a[i+1]-a[i])/2)
print(ans)