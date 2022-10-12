recipet = int(input())
count = int(input())
sum = 0

for i in range(count) :
   a,b = map(int,input().split())
   sum = sum + a *b

if sum == recipet :
    print("Yes")
else :
    print("No")