test = int(input())

for i in range(test) :
    k = int(input())
    n = int(input())
    p = [i for i in range(1,n+1)]

    for x in range(k) :
        for y in range(1,n) :
            p[y] += p[y-1]

    print(p[-1])