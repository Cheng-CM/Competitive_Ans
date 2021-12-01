n = int(input())
c = input().split(" ")
c = list(map(int,c))
ans = 0
m = max(c)
for i in range(n):
    ans += m - c[i]
print(ans)