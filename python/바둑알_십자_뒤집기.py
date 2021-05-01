# https://codeup.kr/problem.php?id=6096

game = [[0 for _ in range(19)] for _ in range(19)]
for i in range(19):
    n = list(map(int, input().split()))
    for j in range(19):
        game[i][j] = n[j]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if game[j][y-1] == 0:
            game[j][y-1] = 1
        else:
            game[j][y-1] = 0

        if game[x-1][j] == 0:
            game[x-1][j] = 1
        else:
            game[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(game[i][j], end=' ')
    print()
