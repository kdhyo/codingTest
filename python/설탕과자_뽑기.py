# https://codeup.kr/problem.php?id=6097

h, w = map(int, input().split())
game = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())
arr = []
for i in range(n):
    input1 = list(map(int, input().split()))
    arr.append(input1)

for i in range(n):
    l = arr[i][0]
    d = arr[i][1]
    x = arr[i][2]
    y = arr[i][3]
    game[x-1][y-1] = 1
    for j in range(l-1):
        if d == 0:
            game[x-1][y+j] = 1
        else:
            game[x+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(game[i][j], end=" ")
    print()
