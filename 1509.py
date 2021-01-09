board = [list(map(int,input().split())) for x in range(10)]
player = list(map(int,input().split()))

for i in range(10):
    if player[i] == 1:
        for j in range(9,-1,-1):
            if board[j][i] < 0:
                print(i+1,"fall")
                break
            elif board[j][i] > 0:
                print(i + 1, "crash")
                break
        else:
            print(i + 1, "safe")

