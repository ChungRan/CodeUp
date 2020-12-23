'''
스네이크 배열 고려해야할점
도는 방향
시간되는 값- 역순? 인지
시작되는 위치
머 이정도만 ㅇㅇ
'''


y, x = map(int,input().split())
board = [[0 for _ in range(x + 2)]for _ in range(y + 2)]
for _x in range(x+2):
    board[0][_x] = -1
    board[y + 1][_x] = -1
for _y in range(y+2):
    board[_y][0] = -1
    board[_y][x+1] = -1
# 배열에서 x가 1~x y가 1~y범위인 배열생성.
ENDNUM = x * y

# 도는 방향
direction = 0 #0은 시계 1은 반시계

#시작 위치
cx = x
cy = 1
cd = 1 # 0 = 오 1 = 밑 2 = 왼 3 = 위

#오름차순 내림차순
way = 1 # 1은 증가 -1은 감소
if way == 1:
    start = 1
    end = ENDNUM + 1
elif way == -1:
    start = ENDNUM
    end = 0

for k in range(start,end,way):
    board[cy][cx] = k
    aq = 1
    if ((way == 1) and (k == end - 1)) or ((way == -1) and (k == end + 1)):
        break
    while(aq == 1):
        if cd % 4 == 0:
        #오른쪽방향
            if board[cy][cx+1] == 0:
                cx = cx + 1
                aq = 0
            else:
                if direction == 0:
                    cd += 1
                elif direction == 1:
                    cd -= 1
        elif cd % 4 == 1:
        #아래
            if board[cy + 1][cx] == 0:
                cy = cy + 1
                aq = 0
            else:
                if direction == 0:
                    cd += 1
                elif direction == 1:
                    cd -= 1
        elif cd % 4 == 2:
        #왼쪽
            if board[cy][cx - 1] == 0:
                cx = cx - 1
                aq = 0
            else:
                if direction == 0:
                    cd += 1
                elif direction == 1:
                    cd -= 1

        elif cd % 4 == 3:
        #위
            if board[cy - 1][cx] == 0:
                cy = cy - 1
                aq = 0
            else:
                if direction == 0:
                    cd += 1
                elif direction == 1:
                    cd -= 1


#출력
for _y in range(1,y+1):
    for _x in range(1,x+1):
        print(board[_y][_x],end=" ")
    print()