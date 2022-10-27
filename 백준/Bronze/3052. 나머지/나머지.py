num = []
nm = []
cn = 0

for i in range(10) :
    num.append(int(input()))
    k = num[i] % 42
    if k not in nm :
        nm.append(k)

print(len(nm))
