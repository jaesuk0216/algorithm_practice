n,m = map(int,input().split())

see = set()
for i in range(n) :
    see.add(input())

hear = set()
for i in range(m) :
    hear.add(input())

res = sorted(list(see&hear))

print(len(res))

for i in res :
    print(i)