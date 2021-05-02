# https://codeup.kr/problem.php?id=6091

a, b, c = map(int, input().split())

num = (a if a > b else b) if ((a if a > b else b) > c) else c
result = num

while result % a != 0 or result % b != 0 or result % c != 0:
    result += num

print(result)
