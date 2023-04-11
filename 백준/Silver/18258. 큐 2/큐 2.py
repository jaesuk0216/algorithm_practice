import sys
from collections import deque

n = int(sys.stdin.readline())
quee = deque([])

for _ in range(n) :
    idx= sys.stdin.readline().split()

    if idx[0] == 'push' :
        quee.append(idx[1])

    elif idx[0] == 'pop' :
        if len(quee) == 0 :
            print(-1)
        else :
            print(quee.popleft())

    elif idx[0] == 'size' :
        print(len(quee))

    elif idx[0] == 'empty' :
        if len(quee) == 0 :
            print(1)
        else :
            print(0)

    elif idx[0] == 'front' :
        if len(quee) == 0 :
            print(-1)
        else :
            print(quee[0])

    elif idx[0] == 'back' :
        if len(quee) == 0 :
            print(-1)
        else :
            print(quee[-1])