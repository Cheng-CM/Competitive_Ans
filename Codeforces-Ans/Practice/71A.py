T = int(input())
for _ in range(T):
    a = input()
    if len(a) >= 11:
        print(a[0]+str(len(a)-2)+a[-1])
    else:
        print(a)