cn = int(input())
n = 0

num = list(map(int,input().split()))

count = int(input())

for i in range(cn) :
    if num[i] == count :
        n +=1

print(n)
