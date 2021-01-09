n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

cx = 0
cy = n - 1
cnum = 1
switch = 0

while(True):
    # print("debug")
    # for y in range(n):
    #     for x in range(n):
    #         print(board[y][x], end=" ")
    #     print()
    #

    board[cy][cx] = cnum
    cnum += 1
    if cy == n-1 and cx == n-1:
        break

    if switch == 0:
        if cx < n - 1:
            cy = cy - 1
            cx = cx + 1
        else:
            switch = 1
            cy = cy + 1
    elif switch == 1:
        if cy < n - 1:
            cy = cy + 1
            cx = cx - 1
        else:
            switch = 0
            cx = cx + 1

for y in range(n):
    for x in range(n):
        print(board[y][x],end=" ")
    print()