n = int(input())
max = 101
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]

for i in range(11, max):
    p.append(p[i-1] + p[i-5])


for i in range(n):
    num = int(input())
    print(p[num-1])
