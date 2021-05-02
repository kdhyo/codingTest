# https://codeup.kr/problem.php?id=6090

a, m, d, n = map(int, input().split())

result = a

for i in range(1, n):
    result *= m
    result += d

print(result)
