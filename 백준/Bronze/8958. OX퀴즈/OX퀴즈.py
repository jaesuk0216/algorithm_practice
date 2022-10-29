number= int(input())

for i in range(number) :
    ox = list(input())
    cn = 0
    score = 0
    for j in ox :
        if j == 'O' :
            score +=1
            cn += score
        else :
            score = 0
    print(cn)