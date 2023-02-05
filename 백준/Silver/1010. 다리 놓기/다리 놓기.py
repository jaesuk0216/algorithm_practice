import sys

def fac(n) :
    ans = 1
    for i in range(1,n+1) :
        ans *=i
    return ans

for i in range(int(sys.stdin.readline())) :
    n,r = map(int,sys.stdin.readline().split())
    print(fac(r)//fac(n)//fac(r-n))