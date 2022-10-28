cn = int(input())

num = list(map(int,input().split()))

k = max(num)

for i in range(cn) :
    num[i] = (num[i] / k) * 100

print(sum(num)/cn)