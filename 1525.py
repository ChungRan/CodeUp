board = [list(map(int,input().split())) for _ in range(10)]
newBoard = [[0 for _ in range(10)] for _ in range(10)]

n = int(input())
playerCoord = []
for x in range(n):
    playerCoord.append(list(map(int,input().split())))

for y in range(10):
    for x in range(10):
        c = board[y][x]
        # 물풍선일떄 처리
        if c >= 1:
            newBoard[y][x] = -2
            for k in range(c):
                if y + k + 1 == 10:
                    break
                else:
                    if board[y+k+1][x] >= 0:
                        newBoard[y+k+1][x] = - 2
                    elif board[y+k+1][x] == -1:
                        break
            for k in range(c):
                if y - k - 1 == -1:
                    break
                else:
                    if board[y-k-1][x] >= 0:
                        newBoard[y-k-1][x] = - 2
                    if board[y-k-1][x] == -1:
                        break
            for k in range(c):
                if x + k + 1 == 10:
                    break
                else:
                    if board[y][x+k+1] >= 0:
                        newBoard[y][x+k+1] = - 2
                    if board[y][x+k+1] == -1:
                        break
            for k in range(c):
                if x - k - 1 == -1:
                    break
                else:
                    if board[y][x-k-1] >= 0:
                        newBoard[y][x-k-1] = - 2
                    if board[y][x-k-1] == -1:
                        break
        # 장애물일때
        elif c == -1:
            newBoard[y][x] = -1


# 플레이어 처리
text = []
for k in range(len(playerCoord)):
    if newBoard[playerCoord[k][0]-1][playerCoord[k][1]-1] == 0:
        newBoard[playerCoord[k][0]-1][playerCoord[k][1]-1] = k + 1
        t = "player " + str(k+1) +" survive"
        text.append(t)
    else:
        t = "player " + str(k + 1) + " dead"
        text.append(t)

for y in range(10):
    for x in range(10):
        print(newBoard[y][x],end=" ")
    print()

print("Character Information")
for i in range(len(text)):
    print(text[i],end="")
    if i != len(text) - 1:
        print()
