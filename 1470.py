# y,x = map(int,input().split())
n = int(input())

board = [[0 for _ in range(n)]for _ in range(n)]

cx = 0
cy = 0
r = 0

for t in range(n*n):
    board[cy][cx] = t + 1
    if r == 0:
        if (cy + 1) < n:
            cy = cy + 1
        elif (cy + 1) == n:
            r = 1
            cx = cx + 1
    elif r == 1:
        if (cy - 1) > -1:
            cy = cy - 1
        elif (cy - 1) == -1:
            r = 0
            cx = cx + 1

# 출력
for _y in range(n):
    for _x in range(n):
        print(board[_y][_x],end=" ")
    print()