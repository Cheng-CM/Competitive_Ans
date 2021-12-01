T = int(input())
for t in range(T):
    s = str(input())
    ki = 0
    ans = 0
    for i in range(0,len(s)-4):
        curr = s[i:i+4]
        if curr == "KICK":
            ki += 1
        if i < len(s)-4 and curr + s[i+4] == "START":
            ans += ki
    print("Case #"+ str(t+1) +":",str(ans),flush=True)