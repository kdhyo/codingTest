# https://codeup.kr/problem.php?id=6084&rid=0

h, b, c, s = map(int, input().split())
result = float((((h * b * c * s) / 8) / 1024) / 1024)
print(round(result, 1), "MB")
