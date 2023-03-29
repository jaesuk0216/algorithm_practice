n,m = map(int,input().split())
base_list = list(range(1,n+1))

for _ in range(m) :
    i,j = map(int,input().split())
    tmp = base_list[j-1]
    base_list[j-1] = base_list[i-1]
    base_list[i-1] = tmp

for i in range(n) :
    print(base_list[i], end = ' ')