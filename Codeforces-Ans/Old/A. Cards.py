n = int(input())
string = input()
ans = ""
for i in range(n):
    if string[i] == "n":
        ans = "1 " + ans
    elif string[i] == "z":
        ans += "0 "
print(ans.strip(),flush=True)
