a,b = input().split()
c = int(input())

h = int(a)
m = int(b)


if (c+m) >= 60 :
    plus = (c+m) // 60
    h = plus + h

if h >= 24 :
    h = h-24

print(h, (c+m)%60)