def fac(n) :
    ans = 1
    for i in range(1,n+1) :
        ans *=i
    return ans

def bino(n,r) :
    print((fac(n) // fac(r) // fac(n-r))%10007)

n,r = map(int,input().split())
bino(n,r)