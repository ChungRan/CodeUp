# 문제오류로 배열의 크기를 충분히 잡아둬야함..
n, m, k = map(int,input().split())

d = [[0 for x in range(m+1000)] for x in range(n+1000)]


for x in range(k):
    x1, y1, x2, y2, u = map(int,input().split())
    # d[x1 -1][y1 - 1] = d[x1 -1][y1 - 1] + u
    # d[x2][y2] = d[x2][y2] + u
    #
    # d[x1 - 1][y2] = d[x1 - 1][y2] - u
    # d[x2][y1 - 1] = d[x2][y1 - 1] - u

    d[x1][y1] = d[x1][y1] + u
    d[x2 + 1][y2 + 1] = d[x2 + 1][y2 + 1] + u

    d[x1][y2 + 1] = d[x1][y2 + 1] - u
    d[x2 + 1][y1] = d[x2 + 1][y1] - u

for y in range(n):
    for x in range(m):
        print(d[y][x],end=" ")
    print()

newd = [[0 for x in range(m+1000)] for x in range(n+1000)]
print()

for _y in range(n):
    for _x in range(m):
        if _x == 0 and _y == 0:
            newd[_y][_x] = d[_x][_y]
        elif _y == 0:
            newd[_y][_x] = newd[_y][_x-1] + d[_y][_x]
        elif _x == 0:
            newd[_y][_x] = newd[_y-1][_x] + d[_y][_x]
        else:
            newd[_y][_x] = newd[_y - 1][_x] + d[_y][_x] + newd[_y][_x - 1] - newd[_y - 1][_x - 1]

for y in range(n):
    for x in range(m):
        print(newd[y][x],end=" ")
    print()