test = int(input())
li = set()

for _ in range(test) :
    li.add(input())

li = list(li)

li.sort()
li.sort(key=len)

for i in li :
    print(i)