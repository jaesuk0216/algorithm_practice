n = int(input())

stack = []
ans = []
flag = 0
cur = 1

for _ in range(n) :
    num = int(input())
    while cur <= num :
        stack.append(cur)
        ans.append("+")
        cur +=1

    if stack[-1] == num :
        stack.pop()
        ans.append("-")

    else :
        flag = 1

if flag == 0 :
    for i in ans :
        print(i)
else :
    print("NO")