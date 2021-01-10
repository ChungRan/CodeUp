# 현재 python 통과 이력 0. 5번 케이스까지는 잘 줄이면 가능할 수 도 있을듯? 그 이상은 모르겠음
# 아마 좀더 개선하면 통과할 수 있을것 같은데... 나중을 기약

a, b = map(int,input().split())
x, y, z = map(int,input().split())
# 생명이 태어나기 위한 조건(x), 생명을 유지하기 위한 최소 조건(y), 생명이 죽는 최소 조건(z)
EMPTYNUM = 100

inputBoard = [list(map(int,input().split())) for _ in range(a)]

k = int(input())

board = [[0 for _ in range(b+2)] for _ in range(a+2)]
newBoard = [[0 for _ in range(b+2)] for _ in range(a+2)]

# newBoard 초기화
for _y in range(a+2):
    for _x in range(b+2):
        if _y == 0 or _y == a+1 or _x == 0 or _x == b+1:
            newBoard[_y][_x] = EMPTYNUM

# board 초기화, 값 입력
for _y in range(a+2):
    for _x in range(b+2):
        if _y == 0 or _y == a+1 or _x == 0 or _x == b+1:
            board[_y][_x] = EMPTYNUM
        else:
            board[_y][_x] = inputBoard[_y-1][_x-1]

switch = 0
for time in range(k):
    if(time == 200):
        print("stop k =",k)
        exit()
    for _y in range(a + 2):
        for _x in range(b + 2):
            if board[_y][_x] == EMPTYNUM:
                continue
            else:
                totalNear = board[_y + 1][_x - 1] + board[_y + 1][_x] + board[_y + 1][_x + 1] + board[_y][_x - 1] + board[_y][_x + 1] + board[_y - 1][_x - 1] + board[_y - 1][_x] + board[_y - 1][_x + 1]
                totalNear = totalNear % EMPTYNUM
                if board[_y][_x] == 0:
                    # 생명이 없을때
                    if totalNear == x:
                        newBoard[_y][_x] = 1
                elif board[_y][_x] == 1:
                    # 생명이 있을때
                    if y <= totalNear < z:
                        newBoard[_y][_x] = 1
                    else:
                        newBoard[_y][_x] = 0
                else:
                    print("테이블값 이상",board[_y][_x])
    # 테이블값 이전
    for _y in range(a+2):
        for _x in range(b+2):
            board[_y][_x] = newBoard[_y][_x]



# 출력
for _y in range(a):
    for _x in range(b):
        print(board[_y+1][_x+1],end=" ")
    print()