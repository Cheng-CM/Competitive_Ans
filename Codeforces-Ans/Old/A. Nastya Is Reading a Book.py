n = int(input())
b = list()
for i in range(n):
    f,l = input().split(" ")
    f,l = int(f),int(l)
    b.append((f,l))
c = int(input())
for i,val in enumerate(b):
    if c >= val[0] and c <= val[1]:
        print(len(b)-i)
        break