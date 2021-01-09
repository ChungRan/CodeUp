

board = [[0 for _ in range(101)] for _ in range(101)]


for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for _y in range(y1,y2):
        for _x in range(x1,x2):
            board[_y][_x] = 1

count = 0
for _y in range(101):
    for _x in range(101):
        if board[_y][_x] == 1:
            count += 1

print(count)