n = int(input())

dp = [0] * (n+1)
le = [0] * (n+1)

dp[0] = 1
le[0] = 0

for i in range(1, n+1):
    dp[i] = 9 * dp[i-1] + le[i-1]
    le[i] = 9 * le[i-1] + dp[i-1]
print(dp[n])