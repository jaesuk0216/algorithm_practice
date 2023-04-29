import sys
from collections import deque

n,k = map(int,input().split())
quee = deque([x for x in range(1,n+1)])

print("<",end="")

while len(quee) != 0 :
    for i in range(k-1) :
        quee.rotate(-1)
    print(quee.popleft(), end='')
    if len(quee) != 0 :
        print(", ", end='')
print(">")