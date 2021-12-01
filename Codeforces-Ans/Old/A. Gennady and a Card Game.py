n = input()
hands = input().split(" ")
pl = False
for card in hands:
    if n[0] == card[0] or n[1] == card[1]:
        pl = True
        break
print("YES" if pl else "NO", flush=True)
