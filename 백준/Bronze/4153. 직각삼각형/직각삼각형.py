while True :
    x = list(map(int,input().split()))
    x.sort()
    if sum(x) == 0 :
        break
    if x[0]**2 + x[1]**2 == x[2]**2 :
        print('right')
    else :
        print('wrong')