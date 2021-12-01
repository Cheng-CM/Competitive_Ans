T = int(input())
if T > 100:
    T = 100
for t in range(T):
    ans = 0
    numOfHouse,budget = input().split(" ")
    houses = input().split(" ")
    houses = sorted(list(map(int, houses)))
    budget = int(budget)
    numOfHouse = int(numOfHouse)
    for i in range(numOfHouse):
        if (budget - houses[i]) >= 0:
            budget -= houses[i]
            ans += 1
        else:
            break
    print("Case #"+str(t+1)+":",ans, flush=True)