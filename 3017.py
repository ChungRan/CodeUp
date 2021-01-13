n = int(input())
board = []

for i in range(n):
    a, b = map(int, input().split())
    board.append([a, b, i + 1])

for i in range(n-1):
    for j in range(n-1-i):
        if board[j][0] > board[j+1][0] or (board[j][0] == board[j+1][0] and board[j][1] > board[j+1][1]) or (board[j][0] == board[j+1][0] and board[j][1] == board[j+1][1] and board[j][2] < board[j+1][2]):
            board[j], board[j+1] = board[j+1], board[j]

for i in range(n-1, -1, -1):
    print(board[i][2], board[i][0], board[i][1])