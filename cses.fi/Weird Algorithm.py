n = int(input())
w_algo = lambda a: a//2 if a % 2 == 0 else a*3+1
ans = [n]
while ans[-1] != 1:
    ans.append(w_algo(ans[-1]))
print(" ".join(list(map(str,ans))))