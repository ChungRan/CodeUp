y,x = map(int,input().split())

for _y in range(y,0,-1):
    de = (_y-1) * x
    for _x in range(1,x+1):
        print(de + _x,end=" ")
    print()