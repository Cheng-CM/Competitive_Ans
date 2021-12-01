n = int(input())
ans = ""
for i in range(n):
    s = input()
    if s[-2:] == "po":
        ans += "FILIPINO\n"
    elif s[-5:] == "mnida":
        ans += "KOREAN\n"
    else:
        ans += "JAPANESE\n"
print(ans)
