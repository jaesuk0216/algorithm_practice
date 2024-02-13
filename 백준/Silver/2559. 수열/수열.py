import sys

input = sys.stdin.readline

day, num = map(int,input().split())
lst = list(map(int,input().split()))

res = []
res.append(sum(lst[:num]))

for i in range(day-num) :
    res.append(res[i]-lst[i]+lst[num+i])

print(max(res))
