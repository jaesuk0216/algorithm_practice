import sys


n = int(sys.stdin.readline())

tem = dict()

for _ in range(n) :
    a,b = map(str,sys.stdin.readline().split())

    if b == "enter" :
        tem[a] = b

    elif b == "leave" :
        del tem[a]

tem = sorted(tem.keys(),reverse = True)

for i in tem :
    print(i)