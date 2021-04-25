# https://codeup.kr/problem.php?id=6085

w, h, b = map(int, input().split())
result = float((((w * h * b) / 8) / 1024) / 1024)
print("{0:0.2f}".format(result), "MB")
