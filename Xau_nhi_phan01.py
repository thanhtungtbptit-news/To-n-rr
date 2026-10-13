a, b = map(int,input().split())

dp = [0] * (a+1)

for i in range(k):
    dp[i] = 2**i

for i in range(k,n+1):
    for j in range (1, k+1):
        dp[i] += dp[i-j]

print(dp[n])
