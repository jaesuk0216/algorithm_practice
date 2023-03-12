pado = [0 for i in range(101)]
pado[1] = 1
pado[2] = 1
pado[3] = 1

for i in range(0,98) :
    pado[i+3] = pado[i] + pado[i+1]

t = int(input())
for i in range(t) :
    n = int(input())
    print(pado[n])