import sys

n = int(sys.stdin.readline())
stack= []

for _ in range(n) :
    idx= sys.stdin.readline().split()

    if idx[0] == 'push' :
        stack.append(idx[1])

    elif idx[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())

    elif idx[0] == 'size' :
        print(len(stack))

    elif idx[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif idx[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])