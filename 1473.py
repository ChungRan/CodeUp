y,x = map(int,input().split())
board = [[0 for _ in range(x)]for _ in range(y)]

cx = x-1
cy = y-1
r = 0

# n = int(input())
# board = [[0 for _ in range(n)]for _ in range(n)]

# cx = n-1
# cy = n-1
# r = 0

for t in range(x*y):
    # print("debug,",cy,cx,r,t)
    board[cy][cx] = t + 1
    if r == 0:
        if (cx - 1) >= 0:
            cx = cx - 1
        elif (cx - 1) < 0:
            r = 1
            cy = cy - 1
    elif r == 1:
        if (cx + 1) <= (x - 1):
            cx = cx + 1
        elif (cx + 1) > (x - 1):
            r = 0
            cy = cy - 1

# 출력
# for _y in range(n):
#     for _x in range(n):
#         print(board[_y][_x],end=" ")
#     print()

for _y in range(y):
    for _x in range(x):
        print(board[_y][x - _x - 1],end=" ")
    print()
# print(board)