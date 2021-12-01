T = int(input())
for t in range(T):
    a = input()
    if int(a[-1]) % 2 == 0:
        print('0')
    else: 
        flag = 1
        for i,v in enumerate(a):
            if i == 0 and int(v) % 2 == 0:
                print('1')
                flag = 0
                break
            elif int(v) % 2 == 0:
                print('2')
                flag = 0
                break
        if flag == 1:
            print('-1')