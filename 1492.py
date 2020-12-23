n = int(input())
board = list(map(int,input().split()))

newboard = []

for x in range(n):
    if x == 0:
        newboard.append(board[x])
    elif x > 0:
        a = newboard[x-1] + board[x]
        newboard.append(a)

for x in newboard:
    print(x,end= " ")