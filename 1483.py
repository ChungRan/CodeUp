y, x = map(int,input().split())
board = [[0 for _ in range(x)]for _ in range(y)]

cx = 0
cy = y - 1
cl = 1

'''
라인의 갯수는 x + y - 1 줄의 길이는 +1 되다가 줄이 y번째일때 최고를 찍고 다음부터는 감소한다.

'''

for t in range(x*y):
    # for _y in range(y):
    #     for _x in range(x):
    #         print(board[_y][_x], end=" ")
    #     print()

    board[cy][cx] = t + 1
    if cx == x - 1 or cy == y - 1:
        cl = cl + 1
        cx = (0 if cl < y else cl - y)
        cy = (y - cl if cl < y else 0)
    else:
        cy = cy + 1
        cx = cx + 1

# 출력
for _y in range(y):
    for _x in range(x):
        print(board[_y][_x],end=" ")
    print()

# print(board)