n = int(input())
a = list(map(int,input().split()))
m = int(input())
qu = list(map(int,input().split()))
for i in range(n-1):
    a[i+1] += a[i]
for q in qu:
    lo,hi = 0,n-1
    while hi >= lo:
        mid = (hi+lo)//2
        if mid == 0 or mid == n-1 or a[mid] >= q > a[mid-1]:
            break
        elif a[mid] > q:
            hi = mid-1
        else:
            lo = mid+1
    print(mid+1)
        