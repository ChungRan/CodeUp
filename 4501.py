board = []
for x in range(7):
    board.append(int(input()))

board.sort()
print(board[6])
print(board[5])