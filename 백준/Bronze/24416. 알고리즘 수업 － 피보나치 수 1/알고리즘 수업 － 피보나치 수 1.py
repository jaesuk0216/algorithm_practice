def fibo(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

def fibo_dp(n) :
    dp = [0] *(n+1)
    dp[1],dp[2] = 1,1
    cnt = 0
    for i in range(3, n+1) :
        cnt +=1
        dp[i] = dp[i-1] + dp[i-2]
    return cnt

n = int(input())
print(fibo(n),fibo_dp(n))
