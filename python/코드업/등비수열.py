# https://codeup.kr/problem.php?id=6089

a, r, n = map(int, input().split())
result = a

for i in range(1, n):
    result *= r

print(result)
