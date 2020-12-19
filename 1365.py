n = int(input())


board = [[' ' for x in range(n-2)]for y in range(n-2)]

for x in range(n-2):
    board[x][x] = '*'
    board[x][n-3-x] = "*"

for x in range(n):
    if((x == 0)or(x == n-1)):
        print('*' * n)
    else:
        print('*' + ''.join(board[x-1]) + '*')