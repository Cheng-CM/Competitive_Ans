n,m,a = list(map(int,input().split()))
d1,m1 = divmod(n,a)
d2,m2 = divmod(m,a)
if m1 > 0: d1 += 1
if m2 > 0: d2 += 1
print(d1 * d2)