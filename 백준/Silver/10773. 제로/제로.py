import sys

k = int(sys.stdin.readline())
li= []

for _ in range(k) :
    num = int(input())
    if num == 0 :
        li.pop()
    else :
        li.append(num)
print(sum(li))