import sys

test = int(sys.stdin.readline())
li = []

for _ in range(test) :
    li.append(list(sys.stdin.readline().split()))
li.sort(key = lambda x: int(x[0]))

for i in li :
    print(i[0],i[1])