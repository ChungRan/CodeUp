y,x = map(int,input().split())

for _y in range(1,y+1):
    for _x in range(1,x+1):
        num = y*(x-_x) + y -_y + 1
        print(str(num),end=" ")
    print()