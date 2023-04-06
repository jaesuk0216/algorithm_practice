import sys

n = int(sys.stdin.readline())



for _ in range(n) :
    stack= []
    ps = sys.stdin.readline()
    for i in ps:
        if i == '(' :
             stack.append('i')
        elif i == ')' :
            if stack :
                stack.pop()
            else :
                print("NO")
                break

    else :
        if not stack :
            print("YES")
        else :
            print("NO")