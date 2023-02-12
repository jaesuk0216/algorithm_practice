N,M = map(int,input().split())

def cnt(n,k) :
    count = 0
    while n :
        n //= k
        count +=n
    return count

five_count = cnt(N,5) - cnt(M,5) - cnt(N-M,5)
two_count = cnt(N,2) - cnt(M,2) - cnt(N-M,2)

ans = min(five_count,two_count)
print(ans)