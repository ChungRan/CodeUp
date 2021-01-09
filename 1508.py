n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i][0] = int(input())

for y in range(n):
    for x in range(y + 1):
        if x > 0 and y > 0:
            board[y][x] = board[y][x-1] - board[y-1][x-1]


for y in range(n):
    for x in range(y + 1):
        print(board[y][x],end=" ")
    print()
