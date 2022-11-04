num = int(input())
cn = 0

for i in range(1, num+1) :
    num = list(map(int,str(i)))
    if i < 100 :
        cn += 1

    elif    num[0] - num[1] == num[1] - num[2] :
        cn +=1

print(cn)