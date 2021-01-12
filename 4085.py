m, n, x, y = map(int,input().split())

# 가로 m 세로 n 땅의 크기
# 가로 x 세로 y 농사할 땅의 크기

board = [list(map(int,input().split())) for _ in range(n)]

tx = m - x + 1
ty = n - y + 1

biggest = 0
for _y in range(ty):
    for _x in range(tx):
        add = 0
        for addY in range(y):
            for addX in range(x):
                add += board[_y + addY][_x + addX]
        if add > biggest:
            biggest = add
print(biggest)