a,b = input().split()

a = list(a)
b = list(b)

a.reverse()
b.reverse()

if a > b :
    print(''.join(a))

else :
    print(''.join(b))