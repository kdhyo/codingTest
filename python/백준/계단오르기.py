# https://www.acmicpc.net/problem/2579

n = int(input())
step = [0] * 300
for i in range(n):
    step[i] = int(input())

dp = [0] * 300
dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[2] + step[0], step[2] + step[1])
for i in range(3, n):
    dp[i] = max(step[i] + dp[i-2], step[i] + step[i-1] + dp[i-3])

print(dp[n-1])
