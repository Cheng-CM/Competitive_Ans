a, b = input().split(" ")
a, b = int(a), int(b)
t = 0
while a <= b:
    t += 1
    a += 2 * a
    b += b
print(t,flush=True)