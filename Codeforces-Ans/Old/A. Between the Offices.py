n = int(input())
string = input()
s,f = 0,0
for i in range(n-1):
    if string[i] == "S" and string[i+1] != string[i]:
        s += 1
    elif  string[i] == "F" and string[i+1] != string[i]:
        f += 1
print("YES" if s > f else "NO")