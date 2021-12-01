s = input()
ans1 = ''
for i in range(len(s)):
    if s[i].isupper():
        ans1 += s[i].lower()
    else:
        break
ans2 = ''
if s[0].islower():
    ans2 = s[0].upper()
    for i in range(1,len(s)):
        if s[i].isupper():
            ans2 += s[i].lower()
        else:
            break
if len(ans1) == len(s):
    print(ans1)
elif len(ans2) == len(s):
    print(ans2)
else:
    print(s)