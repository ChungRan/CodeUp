y, x = map(int,input().split())
board = [[0 for _ in range(x)]for _ in range(y)]

cx = x - 1
cy = 0
cl = 1

'''
라인의 갯수는 x + y - 1 줄의 길이는 +1 되다가 줄이 y번째일때 최고를 찍고 다음부터는 감소한다.

'''

for t in range(x*y):
    board[cy][cx] = t + 1
    if cx == 0 or cy == 0:
        cl = cl + 1
        cx = (x - 1 if cl < y else x - 1 - cl + y)
        cy = (cl - 1 if cl < y else y - 1)
    else:
        cy = cy - 1
        cx = cx - 1

# 출력
for _y in range(y):
    for _x in range(x):
        print(board[_y][_x],end=" ")
    print()

# print(board)