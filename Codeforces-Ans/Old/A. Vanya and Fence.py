n,h = input().split(" ")
n,h = int(n),int(h)
fs = input().split(" ")
fs = list(map(int,fs))
ans = 0
for i in range(n):
    if fs[i] <= h:
        ans += 1
    else:
        ans += 2
print(ans)