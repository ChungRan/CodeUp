for x in range(9):
    for y in range(4):
        print(str((y+2)) + ' x ' + str(x+1) + ' = ' + str((y+2)*(x+1)).rjust(2),end = '')
        if y<3:
            print('\t',end='')
    if x<8:
        print('\n',end='')