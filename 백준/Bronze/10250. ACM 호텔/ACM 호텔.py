test = int(input())

for i in range(test) :
    h,w,n = map(int,input().split())
    f = n%h
    r = n//h +1
    if n%h == 0 :
        r = n//h
        f = h
    print(f'{f*100+r}')