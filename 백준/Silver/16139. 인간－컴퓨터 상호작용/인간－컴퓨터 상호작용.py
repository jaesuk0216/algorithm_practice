import sys

input = sys.stdin.readline

lst = list(input())

time = int(input())



for _ in range(time) :
    cnt = 0
    c,start,end = input().split()
    start = int(start)
    end = int(end)
    for i in range(end-start+1) :
        if c in lst[start+i] :
            cnt+=1
    print(cnt)
