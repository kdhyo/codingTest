# https://codeup.kr/problem.php?id=6087

n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i)
