xlen, ylen = map(int,input().split())

for y in range(ylen):
    if y == 0 or y == ylen - 1:
        for x in range(xlen):
            if x == 0 or x == xlen -1:
                print("+",end="")
            else:
                print("-",end="")
        print()
    else:
        print("|",end="")
        print(" "*(xlen-2),end="|\n")
