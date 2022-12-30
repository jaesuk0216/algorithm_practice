import sys

cnt = int(sys.stdin.readline())
num_card = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
have_card = list(map(int,sys.stdin.readline().split()))

for i in have_card :
    if i in num_card :
        print(1, end=' ')
    else :
        print(0, end=' ')