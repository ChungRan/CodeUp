y, x = map(int,input().split())

oldboard = [list(map(int,input().split())) for _ in range(y)]
oldboard1 = sum(oldboard, [])

board = [[0 for i in range(x)] for h in range(y)]

count = 0
for _y in range(y):
    for _x in range(x):
        board[_y][_x] = oldboard1[count]
        count += 1

newboard = [[0 for i in range(x)] for h in range(y)]



'''
    아래 + 왼쪽 + 자기 - 대각선
'''
for _y in range(y):
    for _x in range(x):
        if _x == 0 and _y == 0:
            newboard[_y][_x] = board[_x][_y]
        elif _y == 0:
            newboard[_y][_x] = newboard[_y][_x-1] + board[_y][_x]
        elif _x == 0:
            newboard[_y][_x] = newboard[_y-1][_x] + board[_y][_x]
        else:
            newboard[_y][_x] = newboard[_y - 1][_x] + board[_y][_x] + newboard[_y][_x - 1] - newboard[_y - 1][_x - 1]


for _y in range(y):
    for _x in range(x):
        print(newboard[_y][_x],end=" ")
    print()