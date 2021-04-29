# https://codeup.kr/problem.php?id=6094

n = int(input())
k = list(map(int, input().split()))

result = k[0]
for i in range(1, n-1):
    if result > k[i+1]:
        result = k[i+1]

print(result)
