import sys

num_list = []

test = int(input())

for _ in range(test) :
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in num_list :
    print(i)