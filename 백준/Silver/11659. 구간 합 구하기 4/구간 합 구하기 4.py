import sys

input = sys.stdin.readline

n,cnt = map(int,input().split())

lst = list(map(int,input().split()))

final_num=[0]
temp = 0


for i in lst :
    temp += i
    final_num.append(temp)


for _ in range(cnt) :
    i, j = map(int,input().split())
    print(final_num[j]-final_num[i-1])