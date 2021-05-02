# https://codeup.kr/problem.php?id=6098

game = []
for i in range(10):
    game.append(list(map(int, input().split())))

x = 1
y = 1
game[x][y] = 9
while True:
    if game[x][y+1] == 0:
        game[x][y+1] = 9
        y += 1
        continue
    elif game[x+1][y] == 0:
        game[x+1][y] = 9
        x += 1
        continue
    elif game[x][y+1] == 2:
        game[x][y+1] = 9
        break
    elif game[x+1][y] == 2:
        game[x+1][y] = 9
        break
    else:
        break

for i in range(10):
    for j in range(10):
        print(game[i][j], end=" ")
    print()
