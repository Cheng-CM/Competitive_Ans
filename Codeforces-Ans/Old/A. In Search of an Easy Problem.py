n = int(input())
ans = input().split(" ")
ans = list(map(int,ans))
if sum(ans) > 0:
    print("Hard",flush = True)
else:
    print("Easy",flush = True)