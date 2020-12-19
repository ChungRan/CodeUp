get = list(input())
board = list()
for x in range(len(get)):
    if (get[x] == 't'):
        board.append(x+1)

for x in board:
    print(x,end=" ")