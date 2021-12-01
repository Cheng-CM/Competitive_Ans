a = input()
ac = 0
for c in a:
    if c == "a":
        ac += 1
print(len(a) if ac > len(a)/2 else ac * 2 - 1)