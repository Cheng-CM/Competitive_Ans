n  = int(input())
out = "I "
for i in range(n):
    if i % 2 == 0:
        out += "hate "
    else:
        out += "love "
    if i < (n-1):
        out += "that I "
out += "it"
print(out,flush = True)