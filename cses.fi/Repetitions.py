s = input()
ans,curr = 0,1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        curr += 1
    else:
        ans = max(curr,ans)
        curr = 1
ans = max(curr,ans)
print(ans)