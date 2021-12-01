def returnDir(i):
    j = i+1
    ans = ""
    while j < len(s):
        if s[j] not in direction and s[j] not in parsis:
            x,y = returnDir(j)
            ans += y
            j = x
        elif s[j] == ")":
            break
        elif s[j] not in parsis:
            ans += s[j]
        j += 1
    return (j,int(s[i]) * ans)

T = int(input())
for t in range(T):
    s = input()
    direction = {'N','S','E','W'}
    parsis = {'(',')'}
    coors = ""
    i = 0
    while i < len(s):
        if s[i] not in direction and s[i] not in parsis:
            idx,ans = returnDir(i)
            coors += ans
            i = idx
        elif s[i] not in parsis:
            coors += s[i]
            i += 1
        else:
            i += 1
    x,y = 0,0
    for i in coors:
        if i == "E":
            x += 1
        elif i == "S":
            y += 1
        elif i == "W":
            x -= 1
        elif i == "N":
            y -= 1
    #mod ans 10**9
    mod = 10**9
    x,y = x % mod,y % mod
    if abs(x) != x:
        x = x + (10**9+1)
    if abs(y) != y:
        y = y + (10**9+1)
    print("Case #"+ str(t+1) +":",str(x+1),str(y+1),flush=True)