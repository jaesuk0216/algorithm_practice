num = set(range(1,10001))
self_num = set()

for i in range(1,10001) :
    k = i+sum(map(int,str(i)))
    self_num.add(k)

sort_num = sorted(num-self_num)
for i in sort_num :
    print(i)