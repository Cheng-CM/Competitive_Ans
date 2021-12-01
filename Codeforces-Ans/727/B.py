n,T = list(map(int,input().split(' ')))
s = list(input())
for i in range(n):
    s[i] = ord(s[i])-ord('a')+1
    if i > 0:
        s[i] += s[i-1]
for _ in range(T):
    l,r = list(map(int,input().split(' ')))
    if l == 1:
        print(s[r-1])
    else:
        print(s[r-1]-s[l-2])
    