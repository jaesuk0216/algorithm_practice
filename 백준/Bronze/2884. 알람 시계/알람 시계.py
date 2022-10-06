a,b = input().split()

h = int(a)
m = int(b)

if m >= 45 :
    print(h, (m-45))
elif m < 45 :
    if h == 0 :
        h = 24
    print((h-1),(m+15))
