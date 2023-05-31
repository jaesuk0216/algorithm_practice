N,M = map(int,input().split())

bas = [i for i in range(1,N+1)]

for i in range(M) :
    i,j = map(int,input().split())
    tmp = bas[i-1:j]
    tmp.reverse()
    bas[i-1:j] = tmp
    
for i in range(N):
    print(bas[i], end = ' ')