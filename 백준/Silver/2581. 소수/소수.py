n = int(input())
m = int(input())
cnt = 0
num_list = []

for i in range(n,m+1) :
    for j in range(2,i+1) :
        if i % j ==0 :
            if i == j :
                num_list.append(i)
            break
            

if len(num_list) > 0 :
    print(sum(num_list))
    print(min(num_list))

else :
    print(-1)