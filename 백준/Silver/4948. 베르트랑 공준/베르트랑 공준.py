num = 123456*2 +1

num_list = [True] *num

for i in range(2,int(num**0.5)+1) :
    if num_list[i] :
        for j in range(2*i,num,i) :
            num_list[j] = False


def prime(n) :
    cnt = 0
    for i in range(n+1,n*2+1) :
        if num_list[i] :
            cnt +=1

    print(cnt)

while True :
    n = int(input())
    if n == 0 :
        break

    prime(n)