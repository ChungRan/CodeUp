n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

cX, cY = int((n - 1)/2), 0

cNum = 1

while(cNum <= n*n):
    # print("debug",cY,cX,cNum)

    # print("debug")
    # for y in range(n):
    #     for x in range(n):
    #         print(board[y][x], end=" ")
    #     print()


    if (board[cY][cX] == 0):
        board[cY][cX] = cNum
        cNum += 1

    else:
        if cNum % n == 1:
            cY += 1
            if cY == n:
                cY = 0

        else:
            cX = cX + 1
            cY = cY - 1
            if cY == -1:
                cY = n - 1
            if cX == n:
                cX = 0

for y in range(n):
    for x in range(n):
        print(board[y][x],end=" ")
    print()