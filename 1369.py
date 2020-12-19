n,k = map(int,input().split())

board = [[' ' for x in range(n+2)]for y in range(n+2)]

for x in range(1,n+1):
    board[x][1] = '*'
    board[n][x] = '*'
    board[x][n] = '*'
    board[1][x] = '*'

for y in range(1,n):
    for x in range(k+1-(y%k),n+1,k):
        board[y][x] = '*'

for y in range(1,n+1):
    for x in range(1,n+1):
        print(board[y][x],end="")
    print('\n',end='')