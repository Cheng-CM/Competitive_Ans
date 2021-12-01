n,m = input().split(" ")
n,m = int(n),int(m)
ns = input().split(" ")
ms = input().split(" ")
T = int(input())
ans = ""
for t in range(T):
    q = int(input())
    ans += ns[(q % n)-1] + ms[(q % m)-1] + "\n"
print(ans)