s = set()
cnt = 0
n,m = map(int,input().split())
for i in range(n) :
    s.add(input())

for j in range(m) :
    test = input()
    if test in s :
        cnt +=1
print(cnt)
