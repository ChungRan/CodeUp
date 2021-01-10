# import numpy as np
import sys
input = sys.stdin.readline

a, b = map(int,input().split())
x, y, z = map(int,input().split())
# 생명이 태어나기 위한 조건(x), 생명을 유지하기 위한 최소 조건(y), 생명이 죽는 최소 조건(z)

EMPTYNUM = 10

inputBoard = [list(map(int,input().split())) for _ in range(a)]

k = int(input())

board = [[0 for _ in range(b+2)] for _ in range(a+2)]
newBoard = [[0 for _ in range(b+2)] for _ in range(a+2)]

# newBoard 초기화
for _y in range(a+2):
    for _x in range(b+2):
        if _y == 0 or _y == a+1 or _x == 0 or _x == b+1:
            newBoard[_y][_x] = EMPTYNUM

# board 초기화, 값 입력
for _y in range(a+2):
    for _x in range(b+2):
        if _y == 0 or _y == a+1 or _x == 0 or _x == b+1:
            board[_y][_x] = EMPTYNUM
        else:
            board[_y][_x] = inputBoard[_y-1][_x-1]

switch = 0
if k > 400:
    k = 400

for time in range(k):
    # if (time == 400):
    #     print("stop k =", k,"time =",time)
        # a = np.arange(15).reshape(3, 5)
        # print(a)

        # exit()
    if switch == 0:
        for _y in range(a + 2):
            for _x in range(b + 2):
                if board[_y][_x] == EMPTYNUM:
                    continue
                else:
                    totalNear = board[_y + 1][_x - 1] + board[_y + 1][_x] + board[_y + 1][_x + 1] + board[_y][_x - 1] + board[_y][_x + 1] + board[_y - 1][_x - 1] + board[_y - 1][_x] + board[_y - 1][_x + 1]
                    totalNear = totalNear % EMPTYNUM
                    if board[_y][_x] == 0:
                        # 생명이 없을때
                        if totalNear == x:
                            newBoard[_y][_x] = 1
                    else:
                        # 생명이 있을때
                        if y <= totalNear < z:
                            newBoard[_y][_x] = 1
                        else:
                            newBoard[_y][_x] = 0
        switch = 1
    else:
        for _y in range(a + 2):
            for _x in range(b + 2):
                if newBoard[_y][_x] == EMPTYNUM:
                    continue
                else:
                    totalNear = newBoard[_y + 1][_x - 1] + newBoard[_y + 1][_x] + newBoard[_y + 1][_x + 1] + newBoard[_y][_x - 1] + newBoard[_y][_x + 1] + newBoard[_y - 1][_x - 1] + newBoard[_y - 1][_x] + newBoard[_y - 1][_x + 1]
                    totalNear = totalNear % EMPTYNUM
                    if newBoard[_y][_x] == 0:
                        # 생명이 없을때
                        if totalNear == x:
                            board[_y][_x] = 1
                    else:
                        # 생명이 있을때
                        if y <= totalNear < z:
                            board[_y][_x] = 1
                        else:
                            board[_y][_x] = 0
        switch = 0



if switch == 0:
    for _y in range(a):
        te = ""
        for _x in range(b):
            te = te + str(board[_y + 1][_x + 1]) + " "
        print(te)
elif switch == 1:
    for _y in range(a):
        te = ""
        for _x in range(b):
            te = te + str(newBoard[_y + 1][_x + 1]) + " "
        print(te)

# 출력
# if switch == 0:
#     for _y in range(a):
#         for _x in range(b):
#             print(board[_y+1][_x+1],end=" ")
#         print()
# elif switch == 1:
#     for _y in range(a):
#         for _x in range(b):
#             print(newBoard[_y+1][_x+1],end=" ")
#         print()