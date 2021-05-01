# https://codeup.kr/problem.php?id=6095

n = int(input())
game = [[0 for _ in range(19)] for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    game[x-1][y-1] = 1

for x in range(19):
    for y in range(19):
        print(game[x][y], end=' ')
    print()
