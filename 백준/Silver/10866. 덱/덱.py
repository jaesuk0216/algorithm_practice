import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for _ in range(n) :
    idx= sys.stdin.readline().split()

    if idx[0] == 'push_front' :
        d.appendleft(idx[1])

    elif idx[0] =='push_back' :
        d.append(idx[1])

    elif idx[0] == 'pop_front' :
        if len(d) == 0 :
            print(-1)
        else :
            print(d.popleft())

    elif idx[0] == 'pop_back' :
        if(len(d)) == 0 :
            print(-1)
        else :
            print(d.pop())

    elif idx[0] == 'size' :
        print(len(d))

    elif idx[0] == 'empty' :
        if len(d) == 0 :
            print(1)
        else :
            print(0)
    
    elif idx[0] == 'front' :
        if len(d) == 0 :
            print(-1)
        else :
            print(d[0])

    elif idx[0] == 'back' :
        if len(d) == 0 :
            print(-1)
        else :
            print(d[-1])
