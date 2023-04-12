from collections import deque

n = int(input())
quee = deque([i for i in range(1,n+1)])
while(len(quee)>1) :
    quee.popleft()
    num = quee.popleft()
    quee.append(num)

print(quee[0])