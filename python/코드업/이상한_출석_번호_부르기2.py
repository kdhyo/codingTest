# https://codeup.kr/problem.php?id=6093

n = int(input())
k = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(k[i], end=' ')
