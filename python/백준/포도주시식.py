# https://www.acmicpc.net/problem/2156

n = int(input())
w = []
for i in range(n):
    w.append(int(input()))

dp = [0]
dp.append(w[0])

if n > 1:
    dp.append(w[0] + w[1])

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] +
              w[i - 2] + w[i-1], dp[i - 2] + w[i-1]))

print(dp[n])
