T = int(input())
ans = ""
for t in range(T):
    n = int(input())
    if n < 4:
        ans += str(4 - n) + "\n"
    else:
        ans += "0\n" if n % 2 == 0 else "1\n"
print(ans,flush=True)