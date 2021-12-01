T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    ans = ''
    d = {'L':'L','R':'R','U':'D','D':'U'}
    for i,v in enumerate(s):
        ans += d[s[i]]
    print(ans)